import discord
import os
import sys
import asyncio

sys.stdout.reconfigure(line_buffering=True)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ログイン完了！ {client.user} です')

@client.event
async def on_message(message):
    if message.author.bot:  # 自分や他のBotは絶対無視
        return

    print(f"受信: {message.author} → {message.content}")  # デバッグ用

    content = message.content.lower()

    # 1回だけ返信するようにする（複数ワードでも1回）
    if any(k in content for k in ['みょん', 'みょーん', 'ミョン']):
        try:
            await message.channel.send('🔪')
            print("みょーん")
        except Exception as e:
            print(f"送信エラー: {e}")

# ここから下は変更なし
async def main():
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("DISCORD_TOKEN がありません！")
        return
    try:
        await client.start(token)
    except Exception as e:
        print(f"エラー: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())