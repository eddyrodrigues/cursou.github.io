#!/usr/bin/env python
# coding: utf-8

# ## Importações básicas

# In[2]:


import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO


# ## Início código

# In[3]:


wblink='https://www.weather.gov/okx/winter#tab-2'
wblink2='https://www.weather.gov'


# In[4]:


req=requests.get(wblink)


# In[5]:


html_code = BeautifulSoup(req.text, 'html.parser')


# In[6]:


#help(html_code)


# In[7]:


html_code.find_all(id="stsImg", limit=1)


# In[8]:


html_code.find_all(id="stsImg", limit=1)[0].attrs['src']


# In[9]:


link_img = html_code.find_all(id="stsImg", limit=1)[0].attrs['src']
wb_final_img = wblink2+link_img


# In[10]:


wb_final_img


# In[11]:


img_req = requests.get(wb_final_img)


# In[12]:


img_req.status_code


# In[13]:


img_bytes = img_req.content


# In[14]:


tipos = ['jpg', 'png', 'PNG', 'JPG', 'JPEG', 'jpeg']
tipo_final = ''
for tipo in tipos:
    if(tipo in str(img_bytes)):
        tipo_final = tipo
tipo_final


# In[15]:


arquivo = 'previsao_neve.'+tipo_final
arquivo_previsao = open(arquivo, 'wb+')


# In[16]:


arquivo_previsao.write((img_bytes))


# In[17]:


arquivo_previsao.close()


# ## Comparando imagens

# In[18]:


arquivo_temp = open("old_forecast1.PNG", "rb")
D1 = arquivo_temp.read()


# In[19]:


arquivo2 = open('previsao_neve.png', 'rb')
D2 = arquivo2.read()


# In[20]:



if D1 == img_bytes:
    print("True")
    
else:
    print("False")


# In[21]:


if (D1 == img_bytes):
    print("Iguais.")
else:
    print("Não são iguais.")


# In[22]:


arquivo2.close()
arquivo_temp.close()


# ## Codigo Novo com intervalo

# In[23]:


import time

while(True):
    img_req = requests.get(wb_final_img)
    img_bytes = img_req.content
    tipos = ['jpg', 'png', 'PNG', 'JPG', 'JPEG', 'jpeg']
    tipo_final = ''
    for tipo in tipos:
        if(tipo in str(img_bytes)):
            tipo_final = tipo
    tipo_final
    print("tipo do arquivo_baixado", tipo_final)
    arq_pc = open("old_forecast1.PNG", "rb")
    arq_pc_bytes = arq_pc.read()
    arq_pc.close()
    if(img_bytes != arq_pc_bytes):
        arq_pc = open("old_forecast1.PNG", "wb")
        arq_pc.write(img_bytes)
        arq_pc.close()
        print("ImgSalva")
    print("Reiniciando o código")
    time.sleep(5)


# In[ ]:




