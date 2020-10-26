#!/usr/bin/env python
# coding: utf-8

# ## `Kivy` importieren

# In[10]:


import kivy
from kivy.app import App
from kivy.uix.label import Label


# In[11]:


class MyApp(App):
    def build(self):
        return Label(text="Tin's first Kivy app")


if __name__ == "__main__":
    MyApp().run()


# In[ ]:




