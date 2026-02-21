import re

name_to_logo = {
    "Mohammad Navaid": "hdfc-placement.webp",
    "Tausifraja": "hdfc-placement.webp",
    "Vaishali Vineet": "tide.webp",
    "Astha Singh": "Bajaj.webp",
    "Aman Kumar": "first-point-creations.webp",
    "Deepak Pratap": "first-point-creations.webp",
    "Monika Baghel": "first-point-creations.webp",
    "Shobhika Rajput": "suwasthi.webp",
    "Yasha": "capital-boon.webp",
    "Sippal Rani": "capital-boon.webp",
    "Deepika": "capital-boon.webp",
    "Anjali Yadav": "capital-boon.webp",
    "Gaurav": "credit-q.webp",
    "Avneesh Kumar Singh": "d-mart.webp",
    "Puja Kumari": "genpact.webp",
    "Ashfee Khan": "genpact.webp",
    "Komal Maurya": "genpact.webp",
    "Sanjeev Kumar Singh": "oppo.webp",
    "Adarsh Singh": "oppo.webp",
    "Ayush Kumar Pandey": "wipro.webp",
    "Chandan Kumar": "smc.webp",
    "Ishika Agarwal": "icici-bank.webp"
}

with open("/home/oxygen/Desktop/Accurate-Landing-v2/index.html", "r") as f:
    html = f.read()

def replacer(match):
    name = match.group(2)
    current_logo = match.group(3)
    
    # Check if the name matches
    new_logo = None
    for k, v in name_to_logo.items():
        if k.lower() in name.lower():
            new_logo = v
            break
            
    if new_logo and current_logo.endswith(".webp"):
        # We need to replace only the current_logo with new_logo in this specific block
        block = match.group(0)
        return block.replace(current_logo, new_logo)
        
    return match.group(0)

# The HTML looks like this:
# <img src="./images/placement/adarsh-singh.webp" alt="Adarsh Singh" ...
# ...
# <img src="./images/placement-logo/random.webp" alt="Company Logo" ...

# Let's split by Student Card
cards = re.split(r"(<!-- Student.*?-->)", html)
new_html = ""
for card in cards:
    if "alt=\"Company Logo\"" in card and "images/placement/" in card:
        # Extract student name from placement image
        img_match = re.search(r"images/placement/([^.]*)\.webp", card)
        if img_match:
            img_name = img_match.group(1).replace("-", " ")
            student_name = img_name.title()
            
            # Find the appropriate logo
            new_logo = None
            for k, v in name_to_logo.items():
                if k.lower() == student_name.lower():
                    new_logo = v
                    break
            
            if new_logo:
                card = re.sub(r'src="\./images/placement-logo/[^"]+"', f'src="./images/placement-logo/{new_logo}"', card)
                
    new_html += card

with open("/home/oxygen/Desktop/Accurate-Landing-v2/index.html", "w") as f:
    f.write(new_html)

print("Names matched to logos successfully.")
