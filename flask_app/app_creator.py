from flask_app.app_aggregator import create_app

app = create_app()

if __name__ == "__main__":
	app.run()