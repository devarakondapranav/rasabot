from models import Intent, IntentMessage, Template, Story, StoryStep, db
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)


########## Creating a sample intent 
# db.create_all()

# nameInt = Intent(name="greet")
# db.session.add(nameInt)
# db.session.commit()


# intentId = Intent.query.filter_by(name='greet').first().id

# mess1 = IntentMessage(message = "Hello", intent_id = intentId)
# mess2 = IntentMessage(message = "Hey",  intent_id = intentId)

# db.session.add(mess1)
# db.session.add(mess2)
# db.session.commit()


##Creating a text template
# greetTemplate = Template(text = "I am Stark. I love you 3000", name="Welcome greeting")
# db.session.add(greetTemplate)
# db.session.commit()





## Creating a story
# greetStory = Story(name = "Greeting story")
# db.session.add(greetStory)
# db.session.commit()

# storyId = Story.query.filter_by(name = "Greeting story").first().id

# a = StoryStep(isIntent = True,story_id =  storyId    ,  int_or_temp_id = Intent.query.filter_by(name='greet').first().id)

# b = StoryStep(isIntent = False,story_id =  storyId    ,  int_or_temp_id = Template.query.filter_by(name='Welcome greeting').first().id)


# db.session.add(a)
# db.session.add(b)
# db.session.commit()

@app.route('/')
def hello_world():
   return ('Hello World')


@app.route('/viewIntents')
def viewIntents():
	pass






@app.route('/train')
def train():

	f = open("nlu.md", "w")
	all_intents = Intent.query.all()

	for intent in all_intents:
		f.write("\n## intent:" + intent.name + '\n')
		all_messages = IntentMessage.query.filter_by(intent_id=intent.id).all()
		for message in all_messages:
			f.write("- " + message.message +'\n')

	f.close()

	f = open("stories.md", "w")
	all_stories = Story.query.all()
	for story in all_stories:
		f.write("\n## " + story.name + "\n")
		for step in StoryStep.query.filter_by(story_id=story.id).all():
			if(step.isIntent):
				f.write("* " + Intent.query.filter_by(id=step.int_or_temp_id).first().name + "\n")
			else:
				temp = Template.query.filter_by(id=step.int_or_temp_id).first().name.replace(" ", "_")
				f.write("  - utter_" + temp + "\n")


	f.close()

	templates = Template.query.all()


	f = open("domain_sample.yml", "w")
	f.write("intents:\n")
	for intent in all_intents:
		f.write("  - " + intent.name + "\n")

	f.write("\nactions:\n")
	for template in templates:
		f.write("  - utter_" + template.name.replace(" ", "_") + "\n")

	

	f.write("\ntemplates:\n")
	for template in templates:
		f.write("  utter_" + template.name.replace(" ", "_") + ":\n")
		f.write('  - text: "' + template.text + '"\n\n')

	f.close()





	return "Done yo so"






	
if __name__ == '__main__':
	
	app.run(debug=True)

   



# all_intents = Intent.query.all()

# for intent in all_intents:
# 	print("## " + intent.name)
# 	all_messages = IntentMessage.query.filter_by(intent_id=intent.id).all()
	