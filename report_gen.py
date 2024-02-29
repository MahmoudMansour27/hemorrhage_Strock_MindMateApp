# Create html report
# convert html to pdf

from xhtml2pdf import pisa

def convert_html_to_pdf(P_id, gender, age, hyper, heart, avg_g, obs, smk, eye, verb, mot, mod_result):
    report_content = f'''<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Report</title>
    </head>

    <body>

        <br>
        <br>
        <br>

    
        <h1 style = "font-family:'Courier New'; font-size: 40px;">MindMate Patient Report</h1>

        <hr>

        <div class="container">
            <h2>Patient ID: {P_id}</h2>
            <table>
                <th>
                    <tr>
                        <th>Parameter</th>
                        <th>Value</th>
                        <th>Parameter</th>
                        <th>Value</th>
                    </tr>
                </th>
                <tbody>
                    <tr>
                        <td>Gender</td>
                        <td>{gender}</td>
                        <td>GCS</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Age</td>
                        <td>{age}</td>
                        <td>Eye</td>
                        <td>{eye}</td>
                        
                    </tr>
                    <tr>
                        <td>Hypertension</td>
                        <td>{hyper}</td>
                        <td>Verbal</td>
                        <td>{verb}</td>
            
                    </tr>
                    <tr>
                        <td>Heart Disease</td>
                        <td>{heart}</td>
                        <td>Motor</td>
                        <td>{mot}</td>
                    </tr>
                    <tr>
                        <td>Avg Glucose Level</td>
                        <td>{avg_g}</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Obesity</td>
                        <td>{obs}</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Smoking Status</td>
                        <td>{smk}</td>
                        <td></td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
            <br>
            <hr>
            <br>
        </div>

        <div class="container">
            <h2>Patient ID: {P_id} | Model Result: {mod_result}</h2>
            <table class="table table-bordered">
                <tbody>
                    <tr>
                        <td><img src="temp_saves/Adaptive_thresh.png" alt="Adaptive_thresh"></td>
                        <td><img src="temp_saves/chan_vese_segmentation.png" alt="chan_vese_segmentation"></td>
                    </tr>
                    <tr>
                        <td><img src="temp_saves/supervised_segmentation.png" alt="supervised_segmentation"></td>
                        <td><img src="temp_saves/unsupervised_segmentation.png" alt="unsupervised_segmentation"></td>

                    </tr>
                </tbody>
            </table>
        </div>
    </body>

    </html>'''
    with open('temp_saves/report.pdf', "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(report_content, dest=pdf_file)
    
    if not pisa_status.err:
        print(f"PDF generated and saved at temp_saves/report.pdf")
    else:
        print("PDF generation failed")
         


#convert_html_to_pdf(5, 'Male', 50, 'yes', 'yes', 500, 'yes', 'somkes', 4, 2, 3, 'Stroke')

