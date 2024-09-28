import re

import subprocess

patron = re.compile('[0-9]')

file = 'Machine_Learning'
file_out = file+'_Tit_Res'

fil = open(file+'.txt', 'r')
filO = open(file_out+'.txt', 'w')

datos = fil.readlines()
fil.close()


'''
for dd in datos:
 if 'title' in dd or 'abstrac' in dd:
  filO.write(dd)

filO.close()
'''

pal = "Research on brain–computer interfaces (BCIs) has become more democratic in recent decades, and experiments using electroencephalography (EEG)-based BCIs has dramatically increased. The variety of protocol designs and the growing interest in physiological computing require parallel improvements in processing and classiﬁcation of both EEG signals and bio signals, such as electrodermal activity (EDA), heart rate (HR) or breathing. If some EEG-based analysis tools are already available for online BCIs with a number of online BCI platforms (e.g., BCI2000 or OpenViBE), it remains crucial to perform ofﬂine analyses in order to design, select, tune, validate and test algorithms before using them online. Moreover, studying and comparing those algorithms usually requires expertise in programming, signal processing and machine learning, whereas numerous BCI researchers come from other backgrounds with limited or no training in such skills. Finally, existing BCI toolboxes are focused on EEG and other brain signals but usually do not include processing tools for other bio signals. Therefore, in this paper, we describe BioPyC, a free, open-source and easy-to-use Python platform for ofﬂine EEG and biosignal processing and classiﬁcation. Based on an intuitive and well-guided graphical interface, four main modules allow the user to follow the standard steps of the BCI process without any programming skills: (1) reading different neurophysiological signal data formats, (2) ﬁltering and representing EEG and bio signals, (3) classifying them, and (4) visualizing and performing statistical tests on the results. We illustrate BioPyC use on four studies, namely classifying mental tasks, the cognitive workload, emotions and attention states from EEG signals."

dic = "trans -b :es " + '"Research on brain–computer interfaces (BCIs) has become more democratic in recent decades"'
print(dic)

# result = subprocess.run(["trans -b :es ", "hello"], capture_output=True, text=True)

result = subprocess.run(["trans", "-b", ":es", pal], capture_output=True, text=True)

print(result.stdout)
 
 
'''
for dd in datosL:
 p = patron.search(dd)  
 if p == None:
  datosN.append(dd)

print(datosN)
'''



