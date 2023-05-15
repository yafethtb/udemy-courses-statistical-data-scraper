from dataclasses import dataclass

@dataclass(slots = True)
class UdemyCourseData:
    id: int
    title: str
    url: str
    price: float
    currency_symbol: str
    rating: float
    number_reviews: int
    number_students: int
    total_lectures: int
    total_time: str
    published_time: str
    last_update_date: str
    level: str
    category: str
    label: str


SUBCATEGORY = {
    'web development': 8,
    'data science': 558,
    'mobile development': 10,
    'programming language': 12,
    'game development': 14,
    'database design & development': 16,
    'software testing': 18,
    'software engineering': 20,
    'software development tools': 362,
    'no-code development': 575,
    'enterpreneurship': 26,
    'communication': 28,
    'management': 30,
    'sales': 32, 
    'business strategy': 34,
    'operation': 36,
    'project management': 38,
    'business law': 40,
    'business analytics and intelligence': 44,
    'human resources': 48,
    'industry': 50,
    'e-commerce': 354,
    'media': 52,
    'real estate': 58,
    'other business': 60,
    'accounting & bookkeeping': 328,
    'compliance': 532,
    'cryptocurrency & blockchain': 534,
    'economic': 536,
    'finance': 540,
    'finance cert. & exam prep.': 542, 
    'financial modeling & analysis': 544,
    'investing & trading': 546,
    'money management tools': 548,
    'taxes': 550,
    'other finance & accounting': 552,
    'IT certification': 132,
    'network & security': 134,
    'hardware': 136,
    'operating system & server': 138,
    'other IT & software': 140,
    'microsoft': 96,
    'apple': 98,
    'google': 100,
    'SAP': 102,
    'oracle': 106,
    'other office productivity': 108,
    'personal transformation': 142,
    'personal productivity': 144,
    'leadership': 146,
    'career development': 150,
    'parenting & relationship': 152,
    'happiness': 156,
    'esoteric practices': 577,
    'religion & spirituality': 158,
    'personal brand building': 160,
    'creativity': 164,
    'influence': 166,
    'self esteem & confidence': 168,
    'stress management': 170,
    'memory & study skill': 172,
    'motivation': 176,
    'other personal development': 178,
    'food & beverages': 182,
    'gaming': 188,
    'home improvement & gardening': 190,
    'pet care & training': 192,
    'travel': 186,
    'other lifestyle': 194,
    'arts & crafts': 180,
    'beauty & makeup': 184,
    'web design': 6,
    'graphic design & illustration': 110,
    'design tools': 112,
    'UX design': 114,
    'game design': 116,
    '3D animation': 120,
    'fashion design': 122,
    'architectural design': 124,
    'interior design': 128,
    'other design': 130,
    'digital marketing': 62,
    'SEO': 64,
    'social media marketing': 66,
    'branding': 68,
    'marketing fundamental': 70,
    'marketing analytics & automation': 72,
    'PR': 74,
    'paid advertising': 76,
    'video & mobile marketing': 78,
    'content marketing': 80,
    'growth hacking': 86,
    'affiliate marketing': 88,
    'product marketing': 90,
    'other marketing': 94,
    'digital photography': 370,
    'photography': 196,
    'portrait photography': 204,
    'photography tool': 198,
    'commercial photography': 208,
    'video design': 218,
    'other photography': 220,
    'fitness': 222,
    'general health': 224,
    'sports': 226,
    'nutrition & diet': 228,
    'yoga': 230,
    'mental health': 232,
    'martial arts & self defense': 236,
    'safety & first aid': 238,
    'dance': 240,
    'meditation': 242,
    'other health & fitness': 244,
    'instruments': 296,
    'music production': 298,
    'music fundamentals': 300,
    'vocal training': 302,
    'music technique': 304,
    'music software': 306,
    'other music': 308,
    'engineering': 366,
    'humanities': 380,
    'math': 310,
    'science': 312,
    'online education': 523,
    'social science': 376,
    'language learning': 521,
    'teacher training': 527,
    'test prep': 529,
    'other teaching & academics': 525
}