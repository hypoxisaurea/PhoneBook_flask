from flask import Flask, render_template, request
app = Flask(__name__, static_folder = './static')

@app.route('/')
def index():
 	return render_template('index.html')


#저장기능, GET 사용
@app.route('/store/', methods=['GET'])
def store():

    #name과 tel 받아오기
	name = request.args.get('name')
	tel = request.args.get('tel')

    #파일 열어 name과 tel 저장
	file = open('./data/phonebook.txt', 'a')
	data = "%s,%s\n" %(name,tel)
	file.write(data) 
	file.close()
	
    #index.html에 msg 전달
	return render_template('index.html', msg='저장되었습니다')


#검색기능, POST 사용
@app.route('/search', methods=['POST'])
def search():

    #딕셔너리 생성, 파일을 열어 ','를 기준으로 key와 value 삽입
	phonebook = {}
	file = open('./data/phonebook.txt','r')
	for line in file:
		key, value = line.strip().split(',')
		phonebook[key]=value
	
    #index.html에서 name 받아오기
	name = request.form['name']

    #딕셔너리에서 key가 name과 같을 경우 tel 출력, 아닐경우 안내 문구 출력
	for key, value in phonebook.items():
		if key == name:
			tel = phonebook[key]
			break
		else:
			tel = "없는 이름입니다"

	file.close()
	
    #index.html에 msg 전달
	return render_template('index.html', msg= "검색 결과: " + tel)
	
#전체보기, GET 이용
@app.route('/view', methods=['GET'])
def view():
	
    #딕셔너리 생성, 파일을 열어 ','를 기준으로 key와 value 삽입
	phonebook = {}
	file = open('./data/phonebook.txt', 'r')
	
	for line in file:
		key, value = line.strip().split(',')
		phonebook[key]=value

	file.close()

    #view.html에 phonebook 딕셔너리 전달
	return render_template('view.html', phonebook=phonebook)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
