# ✨ NSFW Classifier API (simplify version) ✨
Rest API Written In Python To Classify NSFW Images.

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/TheHamkerCat/)


# Fastest Solution

If you don't want to selfhost it, there's already an instance of this running [here](https://thearq.tech/nsfw_scan?url=https://hamker.me/8ni586l.png)

## Install Locally Or On A VPS

```sh
$ git clone https://github.com/johbs/nsfw

$ cd nsfw

$ sudo pip3 install -U -r requirements.txt --no-cache-dir

$ sudo python3 run.py

With you want to auto start your script, you can install PM2 to Manage (the same of NodeJS)

$ sudo npm install pm2 -g

After Install you can add your Run.py script like this:

$ sudo pm2 start run.py

```

## Classifies

* **Hentai** - Hentai and pornographic drawings
* **Porn** - Pornographic images, sexual acts
* **Drawings** - Safe for work drawings (including anime)
* **Neutral** - Safe for work neutral images
* **Sexy** - Sexually explicit images, not pornography

# Credits

Thanks to https://github.com/GantMan/nsfw_model/ for their model.
