import subprocess
subprocess.Popen(['temp_saves/report.pdf'], shell=False)

import webbrowser
webbrowser.open_new(r'temp_saves/report.pdf')

import os
os.system("temp_saves/report.pdf")


from ironpdf import *
import webbrowser
output_path = 'C:\\Users\\buttw\\OneDrive\\Desktop\\url.pdf'
renderer = ChromePdfRenderer()
pdf = renderer.RenderUrlAsPdf("https://www.google.com/")
pdf.SaveAs(output_path)
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
webbrowser.get('chrome').open(output_path)



import webbrowser
webbrowser.open_new(r'file:///home/mahmoud/Documents/programming%20%F0%9F%A4%A4%EF%B8%8F%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB%EF%B8%8F/projects/python/MindMate%20Project/Project/temp_saves/report.pdf')
