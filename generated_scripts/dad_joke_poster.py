import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

def fetch_dad_jokes():
    url = "https://www.boredpanda.com/30-funny-dad-jokes-2/"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    jokes = []
    for li in soup.select("ul.content > li"):
        jokes.append(li.get_text(strip=True).replace("\n", " "))
    return jokes[:30]

def make_poster(jokes, title="Joke-Power", out_path="Joke-Power.png"):
    width, height = 1200, 800
    bg_color = (30, 30, 30)
    text_color = (255, 255, 255)
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 80)
        font_body = ImageFont.truetype("arial.ttf", 40)
    except Exception:
        font_title = ImageFont.load_default()
        font_body = ImageFont.load_default()

    w_title, h_title = draw.textsize(title, font=font_title)
    draw.text(((width - w_title) / 2, 20), title, font=font_title, fill=text_color)

    padding, y = 50, padding + h_title + 30
    line_h = 60
    for joke in jokes:
        w, _ = draw.textsize(joke, font=font_body)
        draw.text(((width - w) / 2, y), joke, font=font_body, fill=text_color)
        y += line_h
        if y > height - 50:
            break

    img.save(out_path, "PNG")
    print(f"Poster saved to {out_path}")

if __name__ == "__main__":
    jokes = fetch_dad_jokes()
    make_poster(jokes)