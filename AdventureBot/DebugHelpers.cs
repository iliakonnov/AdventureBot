﻿using System;
using System.IO;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot
{
    [PublicAPI]
    public static class DebugHelpers
    {
        public static byte[] Serialize<T>(T obj)
        {
            return MessagePackSerializer.Serialize(obj);
        }

        public static string SerializeJson<T>(T obj)
        {
            var data = Serialize(obj);
            return MessagePackSerializer.ConvertToJson(data);
        }

        public static void Dump<T>(T obj, string output)
        {
            File.WriteAllBytes(output, Serialize(obj));
        }

        public static void DumpJson<T>(T obj, string output)
        {
            File.WriteAllText(output, SerializeJson(obj));
        }

        public static T LoadJson<T>(string input)
        {
            return DeserializeJson<T>(File.ReadAllText(input));
        }

        public static T LoadBinary<T>(string input)
        {
            return Deserialize<T>(File.ReadAllBytes(input));
        }

        public static T Deserialize<T>(byte[] data)
        {
            return MessagePackSerializer.Deserialize<T>(data);
        }

        public static T DeserializeJson<T>(string json)
        {
            var data = MessagePackSerializer.ConvertFromJson(json);
            return MessagePackSerializer.Deserialize<T>(data);
        }

        /// <summary>
        ///   Загружает и возвращает пользователя по id мессенджера и id пользователя
        /// </summary>
        public static BadWrapDisposable<UserContext> LoadUser(int messenger_id, long user_id)
        {
            var ctx = new UserContext(new UserId(messenger_id, user_id));
            var wrap = new BadWrapDisposable<UserContext>(ctx);
            return wrap;
        }
    }

    public class BadWrapDisposable<T> where T: IDisposable
    {
        private static int _counter = 0;
        public T Item;

        public BadWrapDisposable(T item)
        {
            _counter++;
            Console.Error.WriteLine("BadWrapDisposable#{0} is constructed!", _counter);
            Item = item;
        }

        ~BadWrapDisposable()
        {
            Console.Error.WriteLine("BadWrapDisposable#{0} is destructed!", _counter);
            try
            {
                Item.Dispose();
            }
            catch (Exception e)
            {
                Console.Error.WriteLine(e);
                throw;
            }
        }
        
        public static implicit operator T(BadWrapDisposable<T> wrap)
        {
            return wrap.Item;
        }
    }
}