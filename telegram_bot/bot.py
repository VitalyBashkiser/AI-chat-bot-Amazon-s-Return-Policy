from aiogram import Bot, Dispatcher, types, BaseMiddleware

from scraper.scrapy_page import extract_amazon_return_policy
from openai_prompts.prompts import generate_prompt, get_openai_response
from config.settings import settings

amazon_url = 'https://www.amazon.co.uk/gp/help/customer/display.html?nodeId=GKM69DUUYKQWKWX7'
policy_data = extract_amazon_return_policy(amazon_url)

bot = Bot(token=settings.telegram_bot_token)
dp = Dispatcher()


class LoggingMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        print(f"Received message: {message.text}")


dp.update.middleware(LoggingMiddleware())


@dp.message(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! I'm your Amazon Return Policy bot. How can I assist you?")


@dp.message()
async def handle_message(message: types.Message):
    prompt = generate_prompt(language="en", user_query=message.text, policy_data=policy_data)
    response = get_openai_response(prompt)
    await message.reply(response)


if __name__ == '__main__':
    dp.start_polling(bot, skip_updates=True)
