# rewards_bot.py (with screenshot feature)

import os
import json
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ... (बाकी SEARCH_SENTENCES की लिस्ट वैसी ही रहेगी) ...
SEARCH_SENTENCES = [
    "Latest trends in artificial intelligence 2025",
    "How does climate change affect oceans?",
    "Benefits of regular exercise for mental health",
    "Quantum computing explained for beginners",
    "How to start a vertical garden at home",
    "Upcoming NASA space missions to Mars",
    "What is blockchain technology and how does it work?",
    "Natural ways to boost memory and concentration",
    "Top programming languages in demand for 2025",
    "Why do cats purr and what does it mean?",
    "What is artificial intelligence and how does it impact daily life?",
"Latest features in iOS 18 update release",
"How to protect your data from cyber attacks",
"Best smartphones under $500 in 2025",
"What is quantum computing and its real-world applications?",
"Top cloud storage services for small businesses",
"How to build a gaming PC on a budget",
"Latest developments in electric vehicle technology",
"What is 5G technology and how fast is it?",
"Best video editing software for beginners",
"How to set up a smart home security system",
"What is the metaverse and how to access it?",
"Top coding bootcamps with job placement rates",
"How to recover deleted files from your computer",
"Best antivirus software for Windows 11",
"Natural remedies for anxiety and stress relief",
"How to lose weight safely without extreme dieting",
"Benefits of intermittent fasting for health",
"Best exercises for lower back pain relief",
"How to improve your immune system naturally",
"Signs and symptoms of vitamin D deficiency",
"Healthy meal prep ideas for busy professionals",
"How to reduce screen time and digital eye strain",
"Benefits of meditation for mental health",
"What causes insomnia and how to treat it?",
"Best superfoods to include in your diet",
"How to maintain good posture while working",
"Natural ways to lower blood pressure",
"Benefits of drinking lemon water every morning",
"How to deal with seasonal depression effectively",
"Cheapest time to book flights for international travel",
"Best solo travel destinations for women in 2025",
"How to pack light for a two-week vacation",
"Top adventure sports destinations around the world",
"Budget-friendly European cities for backpackers",
"How to get travel insurance for international trips",
"Best apps for language translation while traveling",
"Most Instagram-worthy places to visit this year",
"How to avoid jet lag on long-haul flights",
"Top cultural festivals to experience worldwide",
"Best time to visit Maldives for budget travelers",
"How to travel sustainably and reduce carbon footprint",
"Hidden gems in Southeast Asia for tourists",
"Best travel credit cards with no foreign fees",
"How to stay safe while traveling alone",
"How to write a compelling resume that gets noticed",
"Best online courses for career advancement in 2025",
"How to prepare for job interviews effectively",
"Top skills employers are looking for today",
"How to negotiate salary during job offers",
"Best universities for computer science degrees",
"How to switch careers without starting from scratch",
"Benefits of getting professional certifications",
"How to build a strong LinkedIn profile",
"Best ways to network in your industry",
"How to ask for a promotion at work",
"Top remote work opportunities in tech",
"How to manage work-life balance effectively",
"Best side hustles to earn extra income",
"How to overcome imposter syndrome at work",
"Easy dinner recipes for busy weeknights",
"Best coffee brewing methods for home",
"How to meal prep for the entire week",
"Healthiest cooking oils to use daily",
"What foods boost brain power and memory?",
"How to make sourdough bread from scratch",
"Best kitchen gadgets worth the investment",
"How to grow herbs indoors year-round",
"Traditional Italian pasta recipes authentic",
"Vegan substitutes for common baking ingredients",
"How to properly season cast iron cookware",
"Best restaurants in Tokyo for authentic ramen",
"How to preserve fresh vegetables longer",
"Easy one-pot meals for college students",
"What spices pair well with chicken dishes?",
"How to start a vegetable garden at home",
"Best organic fertilizers for indoor plants",
"How to propagate succulents successfully",
"What flowers bloom in winter months?",
"How to create a butterfly garden design",
"Best low-maintenance plants for beginners",
"How to compost kitchen scraps effectively",
"When to plant tomatoes in different climates",
"How to get rid of garden pests naturally",
"Best soil types for growing roses",
"How to prune fruit trees properly",
"What causes yellow leaves on houseplants?",
"How to grow avocado from seed indoors",
"Best time to water plants in summer",
"How to create a zen garden design",
"What vegetables grow well in containers?",
"How to attract bees to your garden naturally",
"Best workout routines for beginners at home",
"How to train for your first marathon",
"What are the benefits of strength training?",
"Best yoga poses for stress relief",
"How to improve flexibility and mobility",
"What is HIIT training and its benefits?",
"Best swimming techniques for fitness",
"How to prevent sports injuries effectively",
"What supplements are worth taking daily?",
"How to build muscle mass naturally",
"Best cardio exercises for weight loss",
"How to recover from intense workouts",
"What causes muscle cramps during exercise?",
"How to stay motivated for regular exercise",
"Best home gym equipment for small spaces",
"How to save money on a tight budget",
"Best investment strategies for beginners",
"What is compound interest and how it works?",
"How to pay off credit card debt fast",
"Best apps for tracking expenses daily",
"How to build an emergency fund quickly",
"What is the difference between stocks and bonds?",
"How to invest in real estate with little money",
"Best retirement planning strategies by age",
"How to improve your credit score fast",
"What are the benefits of budgeting monthly?",
"How to negotiate bills and monthly payments",
"Best high-yield savings accounts in 2025",
"What insurance coverage do I really need?",
"How to start a successful side business",
"How to learn Spanish quickly and effectively",
"Best books to read for personal development",
"How to improve memory and concentration naturally",
"What are the benefits of reading daily?",
"How to develop critical thinking skills",
"Best online resources for learning coding",
"How to master public speaking and presentations",
"What study techniques work best for retention?",
"How to learn new skills after 40",
"Best ways to stay curious and keep learning",
"How to improve writing skills for work",
"What languages are most valuable to learn?",
"How to develop emotional intelligence",
"Best podcasts for continuous learning",
"How to break bad habits permanently",
"What are the signs of a healthy relationship?",
"How to deal with difficult people at work",
"Best ways to make new friends as an adult",
"How to improve communication skills in marriage",
"What causes social anxiety and how to overcome it?",
"How to set healthy boundaries with family",
"Best conflict resolution strategies for couples",
"How to build confidence and self-esteem",
"What are the benefits of spending time alone?",
"How to forgive someone who hurt you deeply",
"Best ways to support a friend through depression",
"How to deal with toxic people in your life",
"What makes a person genuinely happy?",
"How to practice gratitude for better mental health",
"Latest space exploration missions and discoveries",
"What causes climate change and global warming?",
"How do electric cars actually work?",
"What is CRISPR gene editing technology?",
"Latest breakthrough in cancer research treatment",
"How does the human brain process memories?",
"What are the deepest parts of the ocean?",
"How do solar panels convert sunlight to electricity?",
"What causes earthquakes and can we predict them?",
"Latest discoveries about black holes in space",
"How do vaccines work to prevent diseases?",
"What is the most abundant element in universe?",
"How do dolphins communicate with each other?",
"What causes the northern lights phenomenon?",
"Latest research on aging and longevity",
"How to start a podcast from complete scratch",
"Best cameras for beginner photography enthusiasts",
"How to edit videos like a professional",
"What makes a great Instagram photo?",
"Best drawing techniques for digital art",
"How to write a novel step by step",
"What equipment do YouTubers actually need?",
"How to learn guitar chords for beginners",
"Best free software for music production",
"How to improve your singing voice naturally",
"What makes a painting valuable and collectible?",
"How to start a blog that makes money",
"Best lighting setup for home photography",
"How to write compelling short stories",
"What are the basic principles of good design?",
"Most famous unsolved mysteries in history",
"What really happened to the lost city of Atlantis?",
"How were the Egyptian pyramids actually built?",
"What caused the fall of the Roman Empire?",
"Most influential people who changed the world",
"What life was like during medieval times?",
"How did ancient civilizations navigate the oceans?",
"What were the real causes of World War I?",
"Most significant inventions that changed humanity",
"What happened during the Salem witch trials?",
"How did the internet actually get started?",
"What were the first movies ever made?",
"Most beautiful castles around the world to visit",
"What ancient languages can we still understand?",
"How did people communicate before telephones?",
"Current news and updates from around world",
"Latest political developments in major countries",
"What are today's trending topics on social media?",
"Recent breakthrough scientific discoveries announced",
"Latest celebrity news and entertainment updates",
"Current stock market trends and analysis",
"Recent natural disasters and weather events",
"Latest sports scores and championship results",
"New movie releases and reviews this month",
"Current job market trends by industry",
"Recent technology product launches and reviews",
"Latest fashion trends for this season",
"Current real estate market conditions nationally",
"Recent health and medical news updates",
"Latest environmental conservation efforts worldwide",
    "Best tourist destinations in Japan for nature lovers",
    "Most affordable countries to live in for 2025",
    "How to stay productive while working from home",
    "The psychology behind procrastination",
    "Elon Musk's latest update on the Starship mission",
    "Health benefits of drinking green tea daily",
    "List of the world's longest rivers",
    "Tips for better sleep hygiene",
    "Beginner's guide to investing in the stock market",
    "Difference between Artificial Intelligence and Machine Learning",
    "The future of electric vehicles and battery technology",
    "How to manage exam stress effectively",
    "Tips for creating strong, uncrackable passwords",
    "Which are the happiest countries in the world to live in?",
    "How to grow a successful YouTube channel from scratch",
    "Why is financial literacy important for young adults?",
    "Top 10 scientific discoveries of the last decade",
    "How do volcanoes erupt and what are the types?",
    "Difference between an introvert and an extrovert",
    "Benefits of taking cold showers in the morning",
    "The importance of daily journaling for self-reflection",
    "How to overcome laziness and be more active",
    "Signs that you need a digital detox",
    "Interesting facts about black holes and spacetime",
    "What is the multiverse theory?",
    "Effective time management techniques",
    "Basics of machine learning for non-technical people",
    "Healthy and quick breakfast recipes",
    "What is ChatGPT and how does it function?",
    "Best way to learn Python programming online"

]
COOKIE_FILE_PATH = "bing_cookies.json"

def setup_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def load_cookies(driver):
    print("Loading cookies to log in...")
    if not os.path.exists(COOKIE_FILE_PATH):
        print(f"ERROR: Cookie file '{COOKIE_FILE_PATH}' not found.")
        return False
    with open(COOKIE_FILE_PATH, 'r') as f:
        cookies = json.load(f)
    driver.get("https://www.bing.com")
    for cookie in cookies:
        if 'sameSite' in cookie and cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
            del cookie['sameSite']
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Could not add cookie: {cookie.get('name')}. Error: {e}")
    print("Cookies loaded and cleaned successfully.")
    return True

def main():
    driver = setup_driver()
    if not load_cookies(driver):
        driver.quit()
        return

    print("Refreshing page to apply login and taking a screenshot...")
    driver.get("https://www.bing.com")
    time.sleep(7) # पेज को पूरी तरह लोड होने दें

    # --- यहाँ बदलाव किया गया है ---
    # सबूत के तौर पर एक स्क्रीनशॉट लें
    screenshot_file = "login_status_proof.png"
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved as '{screenshot_file}'. This will prove if login was successful.")
    
    # ... (बाकी सर्च का कोड वैसा ही रहेगा) ...
    used_sentences = set()
    total_searches = 30
    print(f"Starting {total_searches} unique random searches...")
    for i in range(total_searches):
        sentence = random.choice([s for s in SEARCH_SENTENCES if s not in used_sentences])
        used_sentences.add(sentence)
        try:
            search_box = driver.find_element(By.NAME, "q")
            search_box.clear()
            search_box.send_keys(sentence)
            search_box.submit()
            wait_time = random.randint(20, 50)
            print(f"Search #{i + 1}/{total_searches}: '{sentence}'. Waiting for {wait_time} seconds...")
            time.sleep(wait_time)
        except Exception as e:
            print(f"An error occurred during search #{i + 1}: {e}")
            driver.save_screenshot(f"error_screenshot_{i+1}.png")
            continue
    
    driver.quit()
    print("Automation script finished successfully.")

if __name__ == "__main__":
    main()