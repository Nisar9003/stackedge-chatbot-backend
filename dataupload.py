import voyageai
from pinecone import Pinecone
import os

# API Keys — yahan apni keys daalo
VOYAGE_API_KEY = "pa-EvnNNQNb7QtFgnktVzD0PKoXoNG8Qe9J8xdlz6XiSVP"
PINECONE_API_KEY = "pcsk_6gpSmv_HZJptAwkunVqxaswmxgJjtMkn17eW8FRHPfT1XSnN6CMQo2LNpFJV3vKHRLkqFy"

voyage = voyageai.Client(api_key=VOYAGE_API_KEY)
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("stackedge-knowledge")

# ============================================================
# COMPANY DATA
# ============================================================
company_chunks = [
    {
        "id": "company_001",
        "text": "Stack Edge Digital is a premium full-stack digital agency — fastest growing in USA. Tagline: From Vision to Reality! Website: https://stackedgedigital.com Phone: +1 386 251 8639 Email: contact@stackedgedigital.com"
    },
    {
        "id": "company_002",
        "text": "Stack Edge Digital USA Office: 425 W Colonial Dr, Suite 303, Office 341, Orlando, FL 32804. Working Hours: 8:00 AM to 5:00 PM Eastern Standard Time (EST). Working Days: Monday to Friday. OFF: Saturday and Sunday."
    },
    {
        "id": "company_003",
        "text": "Stack Edge Digital has a Pakistan office (Onsite) located in Lahore, Johar Town, PIA Housing Society, near Khayabane-e-Firdousi Road. This is the secondary office — only mention if user specifically asks about Pakistan office or second location."
    },
    {
        "id": "company_004",
        "text": "Stack Edge Digital team size: 10 to 50 employees. Mission: Empower businesses with cutting-edge technology and strategic digital solutions combining full-stack web development with targeted digital marketing. Vision: Be a leading digital agency recognized for transformative web and app solutions. Values: Innovation, Integrity."
    },
    {
        "id": "company_005",
        "text": "Stack Edge Digital Services: 1. Website Development — Full-stack, robust, scalable custom websites. 2. Mobile App Development — iOS and Android custom apps. 3. Digital Marketing — SEO, social media, online campaigns. 4. UI/UX Design and Branding — Intuitive design, brand identity. 5. Virtual Assistant Services — Admin tasks, project management. 6. AI and Machine Learning — Predictive Modelling, ChatGPT Integration, NLP, ML/Deep Learning."
    },
    {
        "id": "company_006",
        "text": "Stack Edge Digital process: Discovery → Planning → Design/Development → Testing → Launch → Support → Performance Review. Technologies: Shopify, Webflow, iOS, Android, Full-stack, AI/ML. For pricing: depends on project, contact directly. For jobs/careers: email contact@stackedgedigital.com"
    },
    {
        "id": "company_007",
        "text": "Stack Edge Digital clients include: Brandetize, Tricension, Swift Fit Events, Green Field Groves, 310 Creative. Client testimonials: Alexzandria O'Gara from Brandetize said they went above and beyond on a complex Shopify project. Michael Lammers from Tricension said they communicate like they are in the next cube. Jessica Herbst from Swift Fit Events praised their communication and site updates."
    },
]

# ============================================================
# PORTFOLIO DATA — Platform wise
# ============================================================
portfolio_chunks = [
    {
        "id": "portfolio_platforms",
        "text": "Stack Edge Digital has worked on these platforms: Kajabi, React JS, Cratejoy, OpenCart, BigCommerce, Squarespace, Angular, WooCommerce, Custom PHP, Wix, Lightspeed, HubSpot, Shopify Plus, Laravel, Magento, Drupal, WordPress, Shopify, Web Apps, Sales/Landing Pages, Shopify Apps. Total 100+ projects completed."
    },
    {
        "id": "portfolio_kajabi",
        "text": "Stack Edge Digital Kajabi projects: 1. Allison Sutter Coaching & Community — A spiritual coaching and intuition development platform for women, offering online courses, books, and mentorship. Link: https://www.allisonsutter.com 2. Pain Cure Clinic — A wellness platform focused on chronic pain relief through mind-body connection, workshops and coaching based on Dr. Sarno's method. Link: https://www.paincureclinic.us"
    },
    {
        "id": "portfolio_reactjs",
        "text": "Stack Edge Digital React JS projects: 1. KangarooHealth — An AI-powered connected care platform with Remote Patient Monitoring (RPM), Chronic Care Management, and virtual health coaching. Link: https://www.kangaroohealth.com"
    },
    {
        "id": "portfolio_cratejoy",
        "text": "Stack Edge Digital Cratejoy projects: 1. Hairstylist Club Box — eCommerce store with custom clothing, accessories, and mystery subscription boxes for hairstylists. Link: https://www.hairstylistclubbox.com 2. LippieBox — Monthly lip balm subscription box delivering 5 full-size lip products every month. Link: https://www.lippiebox.com"
    },
    {
        "id": "portfolio_opencart",
        "text": "Stack Edge Digital OpenCart projects: 1. Print EZ — Online printing store for custom business checks, forms, envelopes and promotional items. Established 2000. Link: https://www.printez.com 2. Cat Evolution — Australian eCommerce store for self-cleaning automatic cat litter boxes. Link: https://catevolution.com.au 3. Boaters Outlet — Marine supplies superstore with boating accessories and safety gear. Family-owned since 1990. Link: https://boatersoutlet.com"
    },
    {
        "id": "portfolio_bigcommerce",
        "text": "Stack Edge Digital BigCommerce projects: 1. Di Bruno Bros — Gourmet food store since 1939. Migration increased orders by 19.5%. Link: https://dibruno.com 2. Dainty Jewells — Modest women's clothing store. Link: https://daintyjewells.com 3. Skullcandy — Global audio brand with multi-currency storefronts. Link: https://www.skullcandy.com 4. Science-Rite CBD — CBD wellness store with nano water-soluble products. Link: https://science-ritecbd.com 5. Rug Fashion Store — Premium area rug store with free shipping. Link: https://www.rugfashionstore.com"
    },
    {
        "id": "portfolio_bigcommerce_2",
        "text": "Stack Edge Digital BigCommerce projects continued: 6. DOPE CBD — CBD marketplace on cbd.co. Link: https://cbd.co/dope 7. Revival Home — Furniture and home decor showroom in Tennessee. Link: https://revivalhome.com 8. Supergut — Gut health supplement store with prebiotic fiber products. Link: https://www.supergut.com 9. Niyis African Supermarket — UK online African and Caribbean grocery superstore with 1000+ products. Link: https://niyis.co.uk"
    },
    {
        "id": "portfolio_squarespace",
        "text": "Stack Edge Digital Squarespace projects: 1. Launchpeer — Software development agency for startups. Link: https://launchpeer.com 2. Wisdom Board — Digital community for board directors and CEOs. Link: https://www.wisdomboard.co 3. Pianokids — Online piano learning for children aged 3-6. Link: https://pianokids.com 4. Paula y Gregorio — Vintage and antique furniture boutique. Link: https://www.paulaygregorio.com 5. Envy Eyes & Wax — Luxury med spa in Hawaii. Link: https://www.envyeyesandwax.com 6. Miiskin — Teledermatology platform with AI mole tracking used by 500,000+ people. Link: https://miiskin.com"
    },
    {
        "id": "portfolio_squarespace_2",
        "text": "Stack Edge Digital Squarespace projects continued: 7. Joe Doucet x Partners — Portfolio of award-winning NYC designer with 50+ patents. Link: http://joedoucet.com 8. Castle Hill Technologies — Process automation for biopharma industry. Link: http://www.castlehilltech.com 9. Daniel George Custom Clothier — Premium bespoke menswear in Chicago and San Francisco. Link: http://www.danielgeorge.com 10. Vive Mas Tours — Woman-owned travel company for Cuba and Colombia tours. Link: https://vivemastours.com 11. The Lolla — Brazilian lifestyle blog. Link: https://www.thelolla.com 12. IDEX Blog — Decentralized cryptocurrency exchange blog. Link: http://blog.idex.io"
    },
    {
        "id": "portfolio_woocommerce",
        "text": "Stack Edge Digital WooCommerce projects: 1. All Hung Up Hangers — Premium luxury closet hangers at Saks Fifth Avenue. Link: https://allhunguphangers.com 2. TunerGoods Auto Spa — Automotive customization shop in Texas with paint protection and ceramic coatings. Link: https://www.tunergoods.com 3. Thriving School Psychologist Collective — Professional development for school psychologists. Link: https://www.thrivingschoolpsych.com 4. Traders4Traders — Forex trading education with funded trader program. Link: https://traders4traders.com 5. GiftCardDeal — Discounted gift cards up to 50% off. Link: https://giftcarddeal.com 6. East Coast Containers Inc — Family-owned shipping container supplier. Link: https://eastcoastcontainersinc.com"
    },
    {
        "id": "portfolio_custom_php",
        "text": "Stack Edge Digital Custom PHP projects: 1. Chalo Pakistan — Premium travel platform for international tourists visiting Pakistan. Link: https://www.chalopakistan.com.pk 2. Papa JoinPapa — Senior care platform connecting older adults with companions. Link: https://www.joinpapa.com 3. Alpha Raven House — Amazon product launch and ranking platform. Link: https://www.alpharavenhouse.com 4. FitnessVWork — Fitness and coaching platform for busy professionals. Link: http://fitnessvwork.com 5. Mega Format — Large format printing company in Brooklyn with 48-hour turnarounds. Link: https://megaformat.net"
    },
    {
        "id": "portfolio_wix",
        "text": "Stack Edge Digital Wix projects: 1. Land and Sky Designs — Interior design studio for hospitality and residential clients. Link: https://www.landandskydesigns.com 2. Mercury Plastics Inc — ISO 9001 certified thermoform packaging manufacturer. Link: https://www.mercuryplasticsinc.com 3. Moreish Sweets — Gourmet Arabic sweets in Abu Dhabi. Link: https://www.moreishsweets.com 4. Regenord — Environmental forestry company in 15+ countries, planted 100 million+ trees. Link: https://www.regenord.com 5. Sixpence Bridal — Sustainable bridal boutique in Ontario. Link: http://sixpencebridal.ca 6. Vibrex — Vibration isolation systems for hospitals and airports since 1949. Link: https://www.vibrex.net 7. G-Med — Global medical community for 1.5 million+ verified doctors. Link: https://www.g-med.info 8. Sharaf DG Solar — UAE largest residential solar company. Link: https://www.solar.sharafdg.com"
    },
    {
        "id": "portfolio_wix_2",
        "text": "Stack Edge Digital Wix projects continued: 9. Eureka Program — Academic research program for high school students with top US university professors. Link: https://www.eurekaprogram.com 10. SoSu.TV — Video production and livestreaming for government agencies. Link: https://www.sosu.tv 11. Pendulum118 — Strategic design consultancy for entrepreneurs. Link: https://www.pendulum118.com 12. NRG CBD — Hemp-derived THC-free CBD products store. Link: https://www.nrgcbd.store 13. Sharaf DG Energy — UAE solar energy company with flexible payment plans. Link: https://www.sdgenergy.com 14. The World Capital Group — Business funding firm with 95% approval rates. Link: https://www.theworldcapitalgroup.com 15. Adina Las Vegas — Modest women's fashion brand. Link: https://www.adinalv.com"
    },
    {
        "id": "portfolio_hubspot_lightspeed",
        "text": "Stack Edge Digital HubSpot projects: 1. LoyaltyLevers — Loyalty consulting firm with Marriott, Disney, IKEA experience. Link: https://www.loyaltylevers.com 2. Foundation IT — IT managed services in UK. Link: https://www.foundation-it.com 3. Pressboard — Branded content analytics trusted by Ford, Chase, Spotify. Link: https://www.pressboardmedia.com 4. Interprefy — Enterprise multilingual solution for 30,000+ events globally. Link: https://www.interprefy.com. Lightspeed projects: 1. Penry Air — Industrial compressed air equipment store. Link: https://www.penryair.com 2. Kitchenall — North America top commercial restaurant equipment distributor. Link: https://www.kitchenall.com"
    },
    {
        "id": "portfolio_shopify_plus",
        "text": "Stack Edge Digital Shopify Plus projects: 1. American Heritage Girls Store — Faith-based organization store for girls aged 5-18. Link: https://store.americanheritagegirls.org 2. TN Smoky Mtn Realty — Real estate agency for Smoky Mountain properties. Link: https://www.tnsmokymtnrealty.com 3. Kasamba — Live psychic reading platform serving 3 million+ users. Link: http://www.kasamba.com 4. Think Goodness — Mission-driven brand collective including Origami Owl worth $250M+. Link: http://www.thinkgoodness.com"
    },
    {
        "id": "portfolio_laravel_magento",
        "text": "Stack Edge Digital Laravel projects: 1. YouthsToday — Global youth community platform by Forbes 30 Under 30 honoree with 100,000+ members. Link: https://www.youthstoday.com 2. My Friend in a Box — Virtual mental health therapy platform matching clients with therapists within 24 hours. Link: https://myfriendinabox.com. Magento projects: 1. Litterbox.com — Premium cat care subscription from AutoPets makers of Litter-Robot. Link: https://www.litterbox.com 2. Better Bilt Products Shop — Metal fabrication for landscape and nursery. Link: https://shop.bbponline.com"
    },
    {
        "id": "portfolio_drupal",
        "text": "Stack Edge Digital Drupal projects: 1. Ship Guitars — Global guitar shipping with 25-70% savings, serving 220+ countries. Link: https://shipguitars.com 2. Bellwether Culture — Hybrid events agency with Emmy-winning production team. Link: https://www.bellwetherculture.com 3. NHATS — Johns Hopkins national research platform for aging trends. Link: https://nhats.org 4. The Hill — Leading US political news website second only to CNN. Link: https://thehill.com 5. TopUniversities QS Rankings — World most widely read university rankings with 1500+ institutions. Link: https://www.topuniversities.com 6. Bigge Crane — America largest crane rental company since 1916. Link: https://www.bigge.com 7. American Craft Council — National nonprofit founded in 1943. Link: https://craftcouncil.org"
    },
    {
        "id": "portfolio_wordpress_shopify",
        "text": "Stack Edge Digital WordPress projects: 1. Ann Arbor Plastic Surgery — Board-certified plastic surgery clinic in Michigan. Link: http://annarborplasticsurgery.com 2. Coastal Valley Dermatology — Dermatology clinic in California. Link: https://coastalvalleydermatology.com 3. Mavrck — Influencer marketing platform trusted by Dunkin and Purina. Link: https://www.mavrck.co 4. The Happy Chicken Coop — Most widely read backyard chicken keeping community. Link: https://www.thehappychickencoop.com 5. Holland Ridge Farms — New Jersey tulip farm with largest pick-your-own tulip experience on US East Coast. Link: https://www.hollandridgefarms.com"
    },
    {
        "id": "portfolio_shopify",
        "text": "Stack Edge Digital Shopify projects: 1. Felix Z Designs — Handmade gemstone jewelry in NYC. Link: https://felixz.com 2. Vezia — Wellness and lifestyle store with supplements and apparel. Link: https://www.veziaco.com 3. Nourish Markets — Chef-crafted organic airport dining at BWI by celebrity chef Robbie Jester. Link: https://www.nourishmarkets.com 4. Go-Readers — Designer reading glasses with free shipping over $50. Link: https://www.go-readers.com 5. Dan Henry Watches — Limited-edition vintage-inspired watches by a collector of 1500+ timepieces. Link: https://danhenrywatches.com"
    },
    {
        "id": "portfolio_webapps",
        "text": "Stack Edge Digital Web Apps projects: 1. Frontline Health — AHA and Red Cross CPR/AED certification training in NYC. Link: https://www.frontlinehealth.com 2. ETTVI — 100+ AI-powered SEO tools platform, no signup needed. Link: https://ettvi.com 3. Apteo — Predictive marketing for Shopify brands, raised $1.1M. Link: https://www.apteo.co 4. SalesRx — Direct marketing agency with World Retail Forum Innovation Award. Link: https://salesrx.biz 5. GoTriage — First AI-based online triage in Middle East. Link: https://apps.apple.com/us/app/gotriage/id1519201473 6. Fortes Education — Virtual learning platform for UAE schools with 40+ years experience. Link: https://forteseducation.com"
    },
    {
        "id": "portfolio_landing_pages",
        "text": "Stack Edge Digital Sales and Landing Pages projects: 1. The Johnny Box Landing Page — 11-piece complete bathroom accessory set. Link: https://www.thejohnnybox.com/pages/lpstm 2. Mind Body Hemp Collections — Woman-owned CBD wellness store. Link: https://mindbodyhemp.com/collections 3. NV Inc Launch Your LLC — Business formation with $6000+ bonuses. Link: https://www.nvinc.com/launch-your-llc-corp 4. TryCGM — Continuous glucose monitoring supplies from $99/month. Link: https://trycgm.com 5. Trader2B — Oldest funded stock trader program since 2010. Link: https://trader2b.com 6. YogaClub — Personalized activewear subscription with premium brands. Link: https://yogaclub.com"
    },
]

all_chunks = company_chunks + portfolio_chunks

def upload_data():
    print(f"Total chunks to upload: {len(all_chunks)}")
    
    texts = [chunk["text"] for chunk in all_chunks]
    
    print("Generating embeddings with Voyage AI...")
    embeddings = voyage.embed(
        texts,
        model="voyage-large-2",
        input_type="document"
    ).embeddings
    
    print("Uploading to Pinecone...")
    vectors = []
    for i, chunk in enumerate(all_chunks):
        vectors.append({
            "id": chunk["id"],
            "values": embeddings[i],
            "metadata": {"text": chunk["text"]}
        })
    
    # Batch upload
    batch_size = 10
    for i in range(0, len(vectors), batch_size):
        batch = vectors[i:i+batch_size]
        index.upsert(vectors=batch)
        print(f"Uploaded batch {i//batch_size + 1}")
    
    print("All data uploaded to Pinecone successfully!")
    print(f"Total vectors: {len(vectors)}")

if __name__ == "__main__":
    upload_data()
