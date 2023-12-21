# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="• مسح •", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="ll", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
            ],
            [
            InlineKeyboardButton(
            text="• ᗩძძ TᏂᥱ ᙖ᥆T T᥆ Y᥆ᥙɾ ᘜɾ᥆ᥙρ •",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
            ],
            [
            InlineKeyboardButton(text="• ᘜᖇ᥆υρ ᥉᥆υᖇᥴᥱ •", url=f"https://t.me/FLS_45"),
            InlineKeyboardButton(text="• ᥴ𝗁ᥲᥒᥒᥱᥣ ᥉᥆υᖇᥴᥱ •", url=f"https://t.me/Mr_Eirux"),
            ],
            [
            InlineKeyboardButton(text="• 𓏺 ⊀𝟑𝟑 𓏺 ժᥱ᥎ Mazen 𓏺 ⊀𝟑𝟑 𓏺 •", url=f"https://t.me/M_LR1"),
            ],
            [
            InlineKeyboardButton(text="• ᥴᥣ᥆᥉ᥱ •", callback_data="close"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="• اضف البوت في مجموعتك •",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="• اوامر التشغيل •", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="• قناة سورس •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• جروب الدعم •", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="• مطور السورس •", url="https://t.me/P_O28"
        ),
        InlineKeyboardButton(text="• مالك البوت •", user_id=config.OWNER_ID),
    ],
    [
    InlineKeyboardButton(
            text="•𓏺 ⊀𝟑𝟑 𓏺 ժᥱ᥎ Mazen 𓏺 ⊀𝟑𝟑 𓏺•", url="https://t.me/M_LR1"
        ),
        ],
        ]
    


gp_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضف البوت في مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="• قناة سورس •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• جروب الدعم •", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="• مطور السورس •", url="https://t.me/P_O28"
        ),
        InlineKeyboardButton(text="• مالك البوت •", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="• اوامر التشغيل •",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="• اوامر المطور •", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="• اوامر المالك •", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="• رجوع •", callback_data="fallen_home"),
        InlineKeyboardButton(text="• مسح •", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="• جروب الدعم •", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="• رجوع •", callback_data="fallen_help"),
        InlineKeyboardButton(text="• مسح •", callback_data="close"),
    ],
]
