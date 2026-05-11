AREAS = [
    {
        "name": "Boracay",
        "description": "White sand beaches and island hopping.",
        "location": "Aklan",
        "region": "Western Visayas",
        "latitude": 11.9674,
        "longitude": 121.9248,
        "category": "beach",
    },
    {
        "name": "Siargao",
        "description": "Surfing capital with lagoons and rock pools.",
        "location": "Surigao del Norte",
        "region": "Caraga",
        "latitude": 9.8482,
        "longitude": 126.0458,
        "category": "beach",
    },
    {
        "name": "Banaue Rice Terraces",
        "description": "Ancient terraces carved into the mountains.",
        "location": "Ifugao",
        "region": "Cordillera",
        "latitude": 16.9104,
        "longitude": 121.0614,
        "category": "cultural",
    },
    {
        "name": "Puerto Princesa Underground River",
        "description": "Protected river cave system and nature park.",
        "location": "Palawan",
        "region": "Mimaropa",
        "latitude": 10.1928,
        "longitude": 118.9263,
        "category": "nature",
    },
    {
        "name": "Cebu City",
        "description": "Historic city with museums and food trips.",
        "location": "Cebu",
        "region": "Central Visayas",
        "latitude": 10.3157,
        "longitude": 123.8854,
        "category": "urban",
    },
    {
        "name": "Baguio",
        "description": "Mountain city known for cool weather.",
        "location": "Benguet",
        "region": "Cordillera",
        "latitude": 16.4023,
        "longitude": 120.5960,
        "category": "mountain",
    },
]

ACTIVITIES = [
    # Boracay (4 activities)
    {
        "area": "Boracay",
        "activity_name": "Island Hopping",
        "description": "Visit nearby islands and beaches.",
        "difficulty_level": "easy",
        "estimated_duration": "4 hours",
        "price_range": "PHP 1500",
    },
    {
        "area": "Boracay",
        "activity_name": "Parasailing",
        "description": "Enjoy aerial views of the island.",
        "difficulty_level": "moderate",
        "estimated_duration": "30 minutes",
        "price_range": "PHP 2500",
    },
    {
        "area": "Boracay",
        "activity_name": "Helmet Diving",
        "description": "Walk underwater and explore marine life.",
        "difficulty_level": "easy",
        "estimated_duration": "45 minutes",
        "price_range": "PHP 1800",
    },
    {
        "area": "Boracay",
        "activity_name": "Sunset Sailing",
        "description": "Relax on a traditional paraw boat at sunset.",
        "difficulty_level": "easy",
        "estimated_duration": "1 hour",
        "price_range": "PHP 800",
    },

    # Siargao (2 activities)
    {
        "area": "Siargao",
        "activity_name": "Surfing Lesson",
        "description": "Learn to surf with local instructors.",
        "difficulty_level": "moderate",
        "estimated_duration": "2 hours",
        "price_range": "PHP 1200",
    },
    {
        "area": "Siargao",
        "activity_name": "Sugba Lagoon Tour",
        "description": "Swim and kayak in the famous lagoon.",
        "difficulty_level": "easy",
        "estimated_duration": "5 hours",
        "price_range": "PHP 2000",
    },

    # Banaue Rice Terraces (3 activities)
    {
        "area": "Banaue Rice Terraces",
        "activity_name": "Terrace Trek",
        "description": "Guided walk through the terraces.",
        "difficulty_level": "moderate",
        "estimated_duration": "3 hours",
        "price_range": "PHP 500",
    },
    {
        "area": "Banaue Rice Terraces",
        "activity_name": "Village Tour",
        "description": "Visit traditional Ifugao villages.",
        "difficulty_level": "easy",
        "estimated_duration": "2 hours",
        "price_range": "PHP 400",
    },
    {
        "area": "Banaue Rice Terraces",
        "activity_name": "Sunrise Viewing",
        "description": "Watch sunrise over the rice terraces.",
        "difficulty_level": "easy",
        "estimated_duration": "1 hour",
        "price_range": "PHP 300",
    },

    # Puerto Princesa Underground River (1 activity)
    {
        "area": "Puerto Princesa Underground River",
        "activity_name": "River Cave Tour",
        "description": "Boat tour inside the underground river.",
        "difficulty_level": "easy",
        "estimated_duration": "1.5 hours",
        "price_range": "PHP 1000",
    },

    # Cebu City (5 activities)
    {
        "area": "Cebu City",
        "activity_name": "Heritage Walk",
        "description": "Visit old churches and museums.",
        "difficulty_level": "easy",
        "estimated_duration": "2 hours",
        "price_range": "PHP 400",
    },
    {
        "area": "Cebu City",
        "activity_name": "Temple Visit",
        "description": "Explore Cebu Taoist Temple.",
        "difficulty_level": "easy",
        "estimated_duration": "1.5 hours",
        "price_range": "PHP 300",
    },
    {
        "area": "Cebu City",
        "activity_name": "Food Tour",
        "description": "Taste Cebu's famous local delicacies.",
        "difficulty_level": "easy",
        "estimated_duration": "3 hours",
        "price_range": "PHP 1200",
    },
    {
        "area": "Cebu City",
        "activity_name": "Mountain Hiking",
        "description": "Hike scenic mountain trails near the city.",
        "difficulty_level": "hard",
        "estimated_duration": "6 hours",
        "price_range": "PHP 900",
    },
    {
        "area": "Cebu City",
        "activity_name": "Whale Shark Watching",
        "description": "Experience swimming with whale sharks.",
        "difficulty_level": "moderate",
        "estimated_duration": "5 hours",
        "price_range": "PHP 2500",
    },

    # Baguio (2 activities)
    {
        "area": "Baguio",
        "activity_name": "Mountain Viewpoints",
        "description": "Stop at scenic viewpoints around the city.",
        "difficulty_level": "easy",
        "estimated_duration": "2 hours",
        "price_range": "PHP 300",
    },
    {
        "area": "Baguio",
        "activity_name": "Strawberry Farm Visit",
        "description": "Pick fresh strawberries at local farms.",
        "difficulty_level": "easy",
        "estimated_duration": "1 hour",
        "price_range": "PHP 250",
    },
]

VECTORS = [
    {
        "area": "Boracay",
        "content": "White sand beaches and island hopping tours.",
    },
    {
        "area": "Siargao",
        "content": "Surf breaks, lagoons, and island vibes.",
    },
    {
        "area": "Banaue Rice Terraces",
        "content": "Mountain terraces and cultural heritage walks.",
    },
    {
        "area": "Puerto Princesa Underground River",
        "content": "Underground river cave tour and nature park.",
    },
    {
        "area": "Cebu City",
        "content": "Historic downtown, food trips, and museums.",
    },
    {
        "area": "Baguio",
        "content": "Cool climate, pine trees, and viewpoints.",
    },
]
