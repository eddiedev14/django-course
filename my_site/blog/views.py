from datetime import date
from django.http import Http404
from django.shortcuts import render

posts = [
    {
        "slug": "nature-at-its-best",
        "title": "Nature At Its Best",
        "description": "Nature its amazing! The amount of inspiration I get when walking in nature is incredible!",
        "image": "nature.jpg",
        "author": "Eddie Santiago",
        "lastUpdated": date(2025, 4, 13),
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque neque ipsum, vulputate ut justo eu, accumsan commodo orci. Sed laoreet bibendum pellentesque. Nam suscipit eu odio non fringilla. Nulla ultrices iaculis mi quis fringilla. Praesent accumsan sapien eros. Aliquam nisi augue, pharetra ut mi eu, bibendum porta arcu. Aliquam posuere nibh et sapien tincidunt, eu tincidunt dui lacinia. Duis luctus, justo ac ultrices aliquam, diam ipsum lobortis lacus, porttitor vestibulum metus odio et ex. Aenean tempor accumsan nunc, eget fermentum ante facilisis sit amet. Etiam ut egestas velit, vitae scelerisque dui.

            Aenean venenatis eros sit amet sodales auctor. Aenean eget eros ut neque imperdiet ultricies vitae ac leo. Maecenas non pellentesque felis, ac vulputate nulla. Praesent id ex eget velit tristique egestas eu sed ipsum. Morbi eget sapien rhoncus, interdum neque sed, euismod erat. Maecenas posuere quis neque id sollicitudin. In aliquam tristique ante ac tempor. Maecenas dignissim, tellus at lobortis rhoncus, nisl ex interdum nibh, vitae rhoncus ante ipsum id risus. Phasellus vitae erat vitae ipsum malesuada volutpat vel eget nunc.

            Nam condimentum pharetra odio, eu porttitor magna ornare vel. Maecenas luctus est at blandit gravida. Sed tempus ligula et dignissim tristique. Mauris tempor nisl in lectus tincidunt, eu ullamcorper orci pulvinar. Nulla sodales mattis urna ac accumsan. Morbi vitae quam in nunc tristique viverra. Nam ac ullamcorper nibh, eu blandit urna. Donec ut urna quis justo gravida suscipit id ac erat. Proin egestas eleifend nunc vel eleifend.
        """
    },
    {
        "slug": "mountain-hiking",
        "title": "Mountain Hiking",
        "description": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "image": "hiking.jpg",
        "author": "Pau Cubarsí Paredes",
        "lastUpdated": date(2025, 2, 10),
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque neque ipsum, vulputate ut justo eu, accumsan commodo orci. Sed laoreet bibendum pellentesque. Nam suscipit eu odio non fringilla. Nulla ultrices iaculis mi quis fringilla. Praesent accumsan sapien eros. Aliquam nisi augue, pharetra ut mi eu, bibendum porta arcu. Aliquam posuere nibh et sapien tincidunt, eu tincidunt dui lacinia. Duis luctus, justo ac ultrices aliquam, diam ipsum lobortis lacus, porttitor vestibulum metus odio et ex. Aenean tempor accumsan nunc, eget fermentum ante facilisis sit amet. Etiam ut egestas velit, vitae scelerisque dui.

            Aenean venenatis eros sit amet sodales auctor. Aenean eget eros ut neque imperdiet ultricies vitae ac leo. Maecenas non pellentesque felis, ac vulputate nulla. Praesent id ex eget velit tristique egestas eu sed ipsum. Morbi eget sapien rhoncus, interdum neque sed, euismod erat. Maecenas posuere quis neque id sollicitudin. In aliquam tristique ante ac tempor. Maecenas dignissim, tellus at lobortis rhoncus, nisl ex interdum nibh, vitae rhoncus ante ipsum id risus. Phasellus vitae erat vitae ipsum malesuada volutpat vel eget nunc.

            Nam condimentum pharetra odio, eu porttitor magna ornare vel. Maecenas luctus est at blandit gravida. Sed tempus ligula et dignissim tristique. Mauris tempor nisl in lectus tincidunt, eu ullamcorper orci pulvinar. Nulla sodales mattis urna ac accumsan. Morbi vitae quam in nunc tristique viverra. Nam ac ullamcorper nibh, eu blandit urna. Donec ut urna quis justo gravida suscipit id ac erat. Proin egestas eleifend nunc vel eleifend.
        """
    },
    {
        "slug": "programming-is-great",
        "title": "Programming is great",
        "description": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday",
        "image": "programming.jpg",
        "author": "Eddie Santiago",
        "lastUpdated": date(2024, 12, 27),
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque neque ipsum, vulputate ut justo eu, accumsan commodo orci. Sed laoreet bibendum pellentesque. Nam suscipit eu odio non fringilla. Nulla ultrices iaculis mi quis fringilla. Praesent accumsan sapien eros. Aliquam nisi augue, pharetra ut mi eu, bibendum porta arcu. Aliquam posuere nibh et sapien tincidunt, eu tincidunt dui lacinia. Duis luctus, justo ac ultrices aliquam, diam ipsum lobortis lacus, porttitor vestibulum metus odio et ex. Aenean tempor accumsan nunc, eget fermentum ante facilisis sit amet. Etiam ut egestas velit, vitae scelerisque dui.

            Aenean venenatis eros sit amet sodales auctor. Aenean eget eros ut neque imperdiet ultricies vitae ac leo. Maecenas non pellentesque felis, ac vulputate nulla. Praesent id ex eget velit tristique egestas eu sed ipsum. Morbi eget sapien rhoncus, interdum neque sed, euismod erat. Maecenas posuere quis neque id sollicitudin. In aliquam tristique ante ac tempor. Maecenas dignissim, tellus at lobortis rhoncus, nisl ex interdum nibh, vitae rhoncus ante ipsum id risus. Phasellus vitae erat vitae ipsum malesuada volutpat vel eget nunc.

            Nam condimentum pharetra odio, eu porttitor magna ornare vel. Maecenas luctus est at blandit gravida. Sed tempus ligula et dignissim tristique. Mauris tempor nisl in lectus tincidunt, eu ullamcorper orci pulvinar. Nulla sodales mattis urna ac accumsan. Morbi vitae quam in nunc tristique viverra. Nam ac ullamcorper nibh, eu blandit urna. Donec ut urna quis justo gravida suscipit id ac erat. Proin egestas eleifend nunc vel eleifend.
        """
    },
    {
        "slug": "tech-trends-2024",
        "title": "Tech Trends 2024",
        "description": "Exploring the latest technological innovations shaping our world this year.",
        "image": "tech.jpg",
        "author": "Pedri Gonzalez",
        "lastUpdated": date(2024, 10, 20),
        "content": """
            Technology continues to evolve at an unprecedented pace. In 2024, artificial intelligence, quantum computing,
            and green energy solutions are redefining industries. Startups are pushing boundaries, while established
            companies race to adopt sustainable and ethical approaches.

            One of the most significant shifts has been the integration of AI into daily life. From personalized education
            to advanced healthcare diagnostics, the applications are nearly limitless. At the same time, new challenges
            related to data privacy and bias are forcing regulators and innovators to collaborate.

            Looking ahead, the convergence of biotech, robotics, and advanced networking could lead to breakthroughs that
            seemed like science fiction only a decade ago. The key is not just innovation, but ensuring accessibility and
            equity across societies.
        """
    },
    {
        "slug": "culinary-journeys",
        "title": "Culinary Journeys",
        "description": "Food is more than sustenance—it’s culture, history, and creativity on a plate.",
        "image": "food.jpg",
        "author": "Santiago Delgado",
        "lastUpdated": date(2024, 6, 2),
        "content": """
            Culinary exploration allows us to connect with different cultures in unique ways. From street food markets
            bustling with life to Michelin-starred restaurants experimenting with molecular gastronomy, every dish tells
            a story. 

            Traditional recipes handed down through generations continue to inspire chefs around the globe, blending
            history with innovation. For many, food is not just about eating but about creating memories, sharing, and
            building community.

            In 2024, sustainability and local sourcing have become central themes. More people are seeking plant-based
            alternatives, reducing waste, and reconnecting with natural ingredients. These changes not only impact our
            health but also the planet we share.
        """
    }
]

def home(request):
    latests_posts = posts[:3]
    return render(request, "blog/home.html", { "posts": latests_posts })

def allPosts(request):
    return render(request, "blog/posts.html", { "posts": posts })

def singlePost(request, path):
    selectedPost = None

    for post in posts:
        if post["slug"] == path:
            selectedPost = post
            break

    if selectedPost is not None:
        return render(request, "blog/singlePost.html", { "post": post })
    else:
        #TODO: Ver video de 404 Page error
        raise Http404()
