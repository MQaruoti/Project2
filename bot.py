import logging
import random
import nest_asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# --- CONFIGURATION ---
TOKEN = os.getenv("BOT_TOKEN")
nest_asyncio.apply()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- QUESTIONS DATABASE ---
QUESTIONS = [
    {
        "q": "من الشاعر الملقب بـ 'عرار' والذي يُعد من أبرز شعراء الأردن؟",
        "options": ["حيدر محمود", "مصطفى وهبي التل", "حبيب الزيودي", "عبد المنعم الرفاعي"],
        "correct": 1
    },
    {
        "q": "أكمل البيت: موطني موطني الجلالُ والجمالُ ... ؟",
        "options": [
            "في رُباك الجميلة",
            "والسناءُ والبهاءُ في رُباك",
            "والعزُّ والمجدُ في سماك",
            "فيك الحياةُ لنا"
        ],
        "correct": 1
    },
    {
        "q": "ما اسم المدينة الأردنية الملقبة بـ 'المدينة الوردية'؟",
        "options": ["جرش", "العقبة", "البتراء", "الكرك"],
        "correct": 2
    },
    {
        "q": "من الشاعر الذي قال: 'هذا الحمى عربيُّ الروحِ والشممِ'؟",
        "options": ["مصطفى وهبي التل", "حيدر محمود", "حبيب الزيودي", "الجواهري"],
        "correct": 1
    },
    {
        "q": "أي شاعر أردني اشتهر بالشعر الوطني والقومي؟",
        "options": ["حبيب الزيودي", "نزار قباني", "إيليا أبو ماضي", "أحمد شوقي"],
        "correct": 0
    },
    {
        "q": "ما المدينة الأردنية التي توصف كثيرًا في الشعر بأنها 'مدينة الورد'؟",
        "options": ["السلط", "إربد", "البترا", "معان"],
        "correct": 2
    },
    {
        "q": "ما البحر الشعري الذي كُتبت عليه أغلب القصائد الوطنية الأردنية؟",
        "options": [
            "البحر الطويل",
            "البحر البسيط",
            "البحر الكامل أو الوافر",
            "بحر الرجز"
        ],
        "correct": 2
    },
    {
        "q": "من الشاعر الذي كتب قصيدة 'يا دجلة الخير'؟",
        "options": [
            "محمد مهدي الجواهري",
            "محمود درويش",
            "حيدر محمود",
            "عرار"
        ],
        "correct": 0
    },
    {
        "q": "ما المقصود بكلمة 'الشمم' في الشعر الوطني الأردني؟",
        "options": [
            "الحزن",
            "القوة البدنية",
            "العزة والرفعة والكبرياء",
            "الهدوء"
        ],
        "correct": 2
    },
    {
        "q": "ما اسم النشيد الوطني الأردني؟",
        "options": [
            "موطني",
            "السلام الملكي الأردني",
            "بلاد العرب أوطاني",
            "فدائي"
        ],
        "correct": 1
    },
    {
        "q": "من الشاعر الذي كتب كلمات النشيد الوطني الأردني؟",
        "options": [
            "حيدر محمود",
            "عرار",
            "عبد المنعم الرفاعي",
            "حبيب الزيودي"
        ],
        "correct": 2
    },
    {
        "q": "لماذا يُكثر الشعراء الأردنيون من ذكر الصحراء والخيول في قصائدهم؟",
        "options": [
            "للدلالة على الطقس",
            "لأنها ترمز للأصالة والشجاعة",
            "لأنها رموز سياحية",
            "للدلالة على الحروب فقط"
        ],
        "correct": 1
    },
    {
        "q": "ما الرمز الذي يستخدمه الشعراء كثيرًا للدلالة على الأردن؟",
        "options": ["البحر", "الثلج", "السيف", "النهر"],
        "correct": 2
    },
    {
        "q": "من قائل البيت: 'أردنُّ أرضُ العزمِ أغنيةُ الظُّبى'؟",
        "options": [
            "مصطفى وهبي التل",
            "حيدر محمود",
            "حبيب الزيودي",
            "إبراهيم طوقان"
        ],
        "correct": 0
    },
    {
        "q": "أي من هذه الأبيات يمدح الأردن؟",
        "options": [
            "أردنُّ يا وطني أفديك من وطنٍ",
            "إذا الشعب يومًا أراد الحياة",
            "وطني لو شُغلت بالخلد عنه",
            "بلادي وإن جارت عليّ عزيزة"
        ],
        "correct": 0
    }
]

# --- START COMMAND ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name

    await update.message.reply_text(
        f"مرحباً بك {user_name} في المسابقة الأدبية والشعرية عن الأردن 🇯🇴\n\n"
        "اضغط /quiz لبدء الاختبار!"
    )

# --- SEND QUESTION ---
async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):

    random_idx = random.randint(0, len(QUESTIONS) - 1)
    q_data = QUESTIONS[random_idx]

    context.user_data['current_q_idx'] = random_idx

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"ans_{i}")]
        for i, opt in enumerate(q_data['options'])
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = f"📚 السؤال الأدبي:\n\n{q_data['q']}"

    if update.callback_query:
        await update.callback_query.edit_message_text(
            text=text,
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            text,
            reply_markup=reply_markup
        )

# --- HANDLE ANSWERS ---
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("ans_"):

        selected = int(data.replace("ans_", ""))
        q_idx = context.user_data.get('current_q_idx')

        correct = QUESTIONS[q_idx]['correct']

        if selected == correct:
            result_text = "✅ إجابة صحيحة! أحسنت 👏"
        else:
            correct_answer = QUESTIONS[q_idx]['options'][correct]
            result_text = f"❌ إجابة خاطئة.\n\nالإجابة الصحيحة: {correct_answer}"

        keyboard = [
            [InlineKeyboardButton("سؤال آخر 🔄", callback_data="next_question")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text=f"📖 {QUESTIONS[q_idx]['q']}\n\n{result_text}",
            reply_markup=reply_markup
        )

    elif data == "next_question":
        await send_question(update, context)

# --- MAIN ---
def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", send_question))
    app.add_handler(CallbackQueryHandler(handle_callback))

    print("البوت يعمل الآن... جرب إرسال /quiz")

    app.run_polling(close_loop=False)

# --- RUN ---
if __name__ == '__main__':
    main()
