import PySimpleGUI as sg
import random

layout = [	
			[sg.Text("Открытый текст: "), sg.InputText(key="-text-")],
			[sg.Text("Ключ: "), sg.InputText(key="-code-") ,sg.Button("Генерация кода")],
			[sg.Output(size=(100, 25))],
			[sg.Button("Зашифровать")]]

window = sg.Window('ЭКИ "Шифр Ришелье"', layout)

while True:
	event, values = window.read()
	if event == "Зашифровать":

		if len(values["-text-"]) == 0:
			print("Ввод не должен пустовать.\n\n")
			continue

		text = "".join(values["-text-"].split())
		codeInp = values["-code-"].replace("(","").replace(")","")
		code = codeInp.split()

		out = []

		texttoremove = text
		for codenums in code:
			outfor = [""]*len(codenums)
			for __ in list(codenums):
				try:
					outfor[int(__)-1] = texttoremove[0]
					texttoremove = texttoremove[1:]
				except:
					pass
			out.append(outfor)

		outtext = ''
		for __ in out:
			outtext += "".join(__) + " "

		print(outtext)
	elif event == "Генерация кода":

		if len(values["-text-"]) == 0:
			print("Ввод не должен пустовать.\n\n")
			continue

		array = range(len("".join(values["-text-"].split())))

		out = []
		outfor = []

		for __ in array:
			outfor.append(__)
			if (random.randint(0,2) == 0 and len(outfor)>2) or __ == array[-1] or len(outfor) == 9:
				out.append(sorted(range(1,len(outfor)+1), key = lambda x: random.random()))
				outfor = []
			
		outtext = ""
		for __ in out:
			outtext += "("+"".join(map(str, __))+") "

		window['-code-'].update(outtext)

	elif event == None:
		sys.exit()