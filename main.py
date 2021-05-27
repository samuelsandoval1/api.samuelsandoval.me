from src import create_app
import os

app = create_app()
def main():
    # PORT = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=PORT)
    app.run()

if __name__ == '__main__':
    main()