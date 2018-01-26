# R_aconteur
Project for HackAZ 2018
Team member: Bengoo Kao
--------------------------------------------------------------------------------
Goal:
Resume contains tremandous amount of info that are ofthen overlooked during the hiring process. Our goal is to exploit
underlaying values of resumes for discovering awesome potential candidates.
--------------------------------------------------------------------------------
Implementation:
1. Import data - Gather keyword from resume files (5,000 x 40 in JSON)
2. ML - train system model for correlation scores between skills, education & job categories(python library: SciKit-Learn)
3. Data visualization - Output analysis diagram and judgement(recommendation level)
--------------------------------------------------------------------------------
Current system model usage: 
1. Enter degree major and return belonging department or college. Give correlation score between departments. Continuous high 
correlation implies high consistency. Certain combinations(or majors) are considered a bonus of interdisciplinary studies.
2. Same usage applies to jobs. Enter profession and return belonging industry. Give correlation between industries. Continuous 
high correlation implies high consistency. Certain combinations are considered a bonus of adaptability.
3. Enter skill and return belonging industry. Check correlation between job industry and education department.
--------------------------------------------------------------------------------
