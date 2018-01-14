import pygal

edu1 = 1
edu2 = 2

exp1 = 1
exp2 = 12

eduvalue1 = 2
eduvalue2 = 2
eduvalue3 = 4

expvalue1 = 2
expvalue2 = 4
expvalue3 = 1

radar_chart = pygal.Radar()
radar_chart.title = 'Personal Advanced Analytic'
radar_chart.x_labels = [edu1,edu2,'Between Education Domain',exp1,exp2,'Between Experience Domain']
radar_chart.add('Candidate', [eduvalue1, eduvalue2, eduvalue3,expvalue1,expvalue2,expvalue3])
radar_chart.render_to_file('1.svg')

#dot - Education
edutop = []

dot_chart = pygal.Dot(x_label_rotation=30)
dot_chart.title = 'Education Categorical'
dot_chart.x_labels = [edutop]
dot_chart.add('Candidate', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])

dot_chart.render_to_file('Edu.svg')

#dot - Experience
exptop = [] 

dot_chart = pygal.Dot(x_label_rotation=30)
dot_chart.title = 'Experience Categorical'
dot_chart.x_labels = [exptop]
dot_chart.add('Candidate', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])

dot_chart.render_to_file('Edu.svg')
