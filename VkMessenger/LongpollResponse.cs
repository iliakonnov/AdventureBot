using System.Diagnostics;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Messenger;
using Newtonsoft.Json;
using VkNet;
using VkNet.Model;

namespace VkMessenger
{
    public class LongpollParameters
    {
        public ulong Timestamp;
        public string Key;
        public string Server;

        public LongpollParameters(LongPollServerResponse longPollServerResponse)
        {
            Timestamp = longPollServerResponse.Ts;
            Key = longPollServerResponse.Key;
            Server = longPollServerResponse.Server;
        }

        public async Task Update(VkApi api, LongpollResponse response)
        {
            switch (response.Failed)
            {
                case null:
                    // No error occurred
                    Timestamp = uint.Parse(response.Timestamp);
                    return;
                case 1:
                    // история событий устарела или была частично утеряна, приложение может получать события далее, используя новое значение ts из ответа.
                    Timestamp = uint.Parse(response.Timestamp);
                    return;
                case 2:
                    // истекло время действия ключа, нужно заново получить key методом groups.getLongPollServer.
                    await Update(api, true, false);
                    return;
                case 3:
                    // информация утрачена, нужно запросить новые key и ts методом groups.getLongPollServer.
                    await Update(api, true, true);
                    return;
                default:
                    // объекты в сообщении об ошибке могут содержат поля, не описанные в документации. Их необходимо игнорировать и не пытаться обработать.
                    // На всякий случай обновляю всё
                    await Update(api, true, true);
                    return;
            }
        }

        private async Task Update(VkApi api, bool key, bool ts)
        {
            var response = await api.Groups.GetLongPollServerAsync(Messenger.GroupId);
            if (key)
            {
                Key = response.Key;
            }

            if (ts)
            {
                Timestamp = response.Ts;
            }
            
            // Про сервер ничего не говорится, но на всякий случай тоже обновляю
            Server = response.Server;
        }

        public string GetUrl(int timeout)
        {
            return $"{Server}?act=a_check&key={Key}&ts={Timestamp}&wait={timeout}";
        }
    }

    public class LongpollResponse
    {
        [JsonProperty("ts")] public string Timestamp;

        [JsonProperty("updates")] public Update[] Updates;

        [JsonProperty("failed")] public int? Failed;
    }

    public class Update
    {
        [JsonProperty("type")] public string Type;

        [JsonProperty("object")] public Message Message;

        [JsonProperty("group_id")] public int GroupId;

        public RecivedMessage ToRecivedMessage()
        {
            long chatId = 0;
            long? replyUserId = null;
            if (Message.ChatId == null)
            {
                Debug.Assert(Message.FromId != null, "Message.FromId != null");
                chatId = (long) Message.FromId;
            }
            else
            {
                chatId = (long) Message.ChatId;
                if (Message.ChatId != Message.FromId)
                {
                    replyUserId = Message.Id;
                }
            }

            return new RecivedMessage
            {
                Text = Message.Body,
                ChatId = new ChatId(Messenger.MessengerId, chatId),
                ReplyUserId = replyUserId
            };
        }
    }
}