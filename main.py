from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    summary = "I am a developer & I am an artist. I would like to say this makes me a unicorn in the developer " \
              "world, having the ability to think analytically and creatively. This would be a common misconception " \
              "as developers and artists are very similar, by nature and in their problem-solving process. This is " \
              "why you will often find developers who are also artists. "

    writer = "At the age of 13, I decided I wanted to write the next 'Great American Novel'. So I sat down with a " \
             "pen and pad of notebook paper, this was the 90's before I could afford a computer, and I started " \
             "writing the first sentence, 'It was a dark and stormy night...'. This is arguably the most cliche " \
             "beginning I could have imagined, yet that is actually what I wrote. I probably thought I was a " \
             "genius at the time. Then I sat there and thought about all the possibilities for the next sentence. " \
             "'It was a dark and stormy night. The old house creaked as the wind and rain whipped itself against its " \
             "walls'. That was dumb so I started again, 'It was a dark and stormy night. The young girl paced the " \
             "four corners of her bedroom, trying not to think of the storm as it rattled against the tin walls of " \
             "her mobile home. Could this finally be the moment her home is ripped off the concrete blocks and " \
             "thrown from the trailer park?' That was also dumb, I wasn't a very good writer at the time. " \
             "\n" \
             "I also had no idead what I was writing about. I just decided to keep writing, almost as " \
             "if the story would be handed to me from the popcorn ceilings or paneled walls of the trailer I actually " \
             "lived in. When I first started programming, I found myself falling in to the same traps I had as a 13 " \
             "year old trying to write the best novel ever written. I tried to start writing the best code ever" \
             "written at line 1, without knowing what I was writing about. Then I refused to read other developer's " \
             "coding solutions, because I didn't want to steal ideas and I wanted to come up with my own plan. It" \
             "took time for me to understand the concept of not reinventing the wheel."

    general = "Data Extractions and Transformations are my favorite challenges of the data process. " \
              "When working through complex data issues, work seems more like a puzzle or a logic problem to be " \
              "solved. In every project, this is the best time for me to learn about my data. When the data seems " \
              "'too good to be true', this is when I invoke methodology from the scientific method and attempt to " \
              "prove it wrong."

    return render_template("about.html", title='About Me',
                           summary=summary,
                           writer=writer,
                           general=general)


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", title="Portfolio Coming Soon")


@app.route("/contact")
def contact():
    email = "bettychitty@outlook.com"
    return render_template("contact.html", title="Contact Me",
                           email=email)


if __name__ == "__main__":
    app.run()