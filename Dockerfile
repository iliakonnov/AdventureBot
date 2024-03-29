# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env
WORKDIR /app
 
COPY src/*.sln src/*/*.csproj ./
RUN for file in $(ls *.csproj); do mkdir -p ${file%.*}/ && mv $file ${file%.*}/; done
RUN dotnet restore

# Copy everything else and build
COPY ./src/* ./
RUN dotnet test -c Release
RUN dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/runtime:6.0
WORKDIR /app/work
COPY ./python /app/python
COPY --from=build-env /app/out /app/bin
ENTRYPOINT ["dotnet", "/app/bin/AdventureBot.dll"]

