# definitions.py

import json


def xodim_qoshish():
    xodim = {}
    input("")


def xodimlarni_korish():
    pass


def xodimni_arxivlash():
    pass


def dastur():
    tanlov = -1
    while tanlov:
        print(
            "0. Chiqish;",
            "1. Xodim qo'shish;",
            "2. Xodimlarni ko'rish;",
            "3. Xodimni arxivlash;",
            sep="\n",
        )

        tanlov = int(input("Nima qilishni tanlang: "))

        match tanlov:
            case 0:
                pass
            case 1:
                xodim_qoshish()
            case 2:
                xodimlarni_korish()
            case 3:
                xodimni_arxivlash()


# git init - bo'sh repo boshlab beradi
# repo (ma'lumot ombori) - dastur
# versiyalari qayd etib boriladigan joydir

# git add - file yoki filelarni kuzatuv/kontrol ga olish
# git commit -kuzatuvdagi/kontroldagi filelarni 
# qayd etish / qayd ostiga olish

# git remote add orgin https://github.com/shox750/4-oy-7-dars-uyga-vazifa-8-topshiriq.git
# origin nomli cloud repo qo'shdik 
# uning lokatsiyasi https://github.com/shox750/4-oy-7-dars-uyga-vazifa-8-topshiriq.git ekan

# git branch 

# git status

# git remote -v

# git commit -m "qayd xabari/izohi"
