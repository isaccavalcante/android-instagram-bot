from uiautomator import device as d
from bs4 import BeautifulSoup
import time
import asyncio


def type_word(word):
    for char in word:
        key_code = ord(char) - 68
        d.press(key_code)

def dump():
    xml = d.dump("screen.xml")
    with open("screen .csv", 'w') as f:
        f.write("text,content-desc" + "\n")
        soup = BeautifulSoup(xml, "html.parser")
        for node in soup.find_all("node"):
            line = f"{node['text']},{node['content-desc']},{node['resource-id']}"
            f.write(line + "\n")
            

def enter_instagram():
    d.press.home()
    d(text="Instagram").click()

def follow_commentators():
    enter_instagram()
    d(description="Search and Explore").click()
    d(text="Search").click()
    d(text="Search").click()
    username = "filipedeschamps"
    type_word(username)
    d(text=username).click()
    d(descriptionContains="at Row 1, Column 1").click()
    d(textContains="View all").click()
    d(resourceId="com.instagram.android:id/row_comment_imageview").click()
    d(text="Follow").click()
    d.press.back()
    # WIP


def pretend_normal_usage():
    d(description="Profile").click()
    d(description="Search and Explore").click()
    d(description="Profile").click()
    d(text="Following").click()

def unfollow_all():
    enter_instagram()
    d(description="Profile").click()
    d(text="Following").click()
    for i in range(100):
        d(text="Following").click()
        if d(text="Unfollow").exists:
            d(text="Unfollow").click()
        print(f"Unfollowed {i + 1} accounts")
        d(text="Follow")[-1].drag.to(textContains="Followers")
        time.sleep(30)

