#Date: 22 june 2023
#Last Edited/Updated: 22 june 2023
#Author: Juma 
#Editor: Brian Kasonde

#Purpose of program: To enables users to switch between screens using button's  on the sidebar panel.



import customtkinter as ctk
#you need to pip installe customtkinter

fontype ='Times New Roman'
primary_theme = '#212121'


window = ctk.CTk()
window.geometry("1000x700")

def home():
	#function to display page 1 content.
	def switch_to_page_1():
		frame.destroy()
		window.update()
		page_1()
		
	#function to display page 2 content.
	def switch_to_page_2():
		frame.destroy()
		window.update()
		page_2()
	
    #function to display page 3 content.
	def switch_to_page_3():
		frame.destroy()
		window.update()
		page_3()

    #function to display page 4 content.
	def switch_to_page_4():
		frame.destroy()
		window.update()
		page_4()
			
	dash_btn = ctk.CTkButton(window, text= "Dashboard", font=(fontype, 16), fg_color= primary_theme, command=home)
	dash_btn.place(rely= 0.1, relx = 0.08, anchor = 'center')
	page_1_btn = ctk.CTkButton(window, text= "Page 1", font=(fontype, 16), fg_color= primary_theme, command=switch_to_page_1)
	page_1_btn.place(rely= 0.2, relx = 0.08, anchor = 'center')
	page_2_btn= ctk.CTkButton(window, text= "Page 2", font=(fontype, 16), fg_color= primary_theme, command=switch_to_page_2)
	page_2_btn.place(rely= 0.3, relx = 0.08, anchor = 'center')
	page_3_btn = ctk.CTkButton(window, text= "Page 3", font=(fontype, 16), fg_color= primary_theme, command=switch_to_page_3)
	page_3_btn.place(rely= 0.4, relx = 0.08, anchor = 'center')
	page_4_btn = ctk.CTkButton(window, text= "Page 4", font=(fontype, 16), fg_color= primary_theme, command=switch_to_page_4)
	page_4_btn.place(rely= 0.5, relx = 0.08, anchor = 'center')
	frame = ctk.CTkFrame(window, height = 700, width= 800)
	frame.pack(side='right')
	screenlabel = ctk.CTkLabel(frame, text= 'WELCOME', font=(fontype, 50))
	screenlabel.place(rely= 0.5, relx = 0.5, anchor = 'center')
	

def page_1():
	#function to return home page content.
	def switch_to_home():
		page_1_frame.destroy()
		window.update()
		home()
		
	dash_btn = ctk.CTkButton(window, text= "Dashboard", font=(fontype, 16), fg_color= primary_theme, command=switch_to_home)
	dash_btn.place(rely= 0.1, relx = 0.08, anchor = 'center')
	page_1_btn = ctk.CTkButton(window, text= "Page 1", font=(fontype, 16), fg_color= primary_theme, command='')
	page_1_btn.place(rely= 0.2, relx = 0.08, anchor = 'center')
	page_2_btn= ctk.CTkButton(window, text= "Page 2", font=(fontype, 16), fg_color= primary_theme, command='')
	page_2_btn.place(rely= 0.3, relx = 0.08, anchor = 'center')
	page_3_btn = ctk.CTkButton(window, text= "Page 3", font=(fontype, 16), fg_color= primary_theme, command='')
	page_3_btn.place(rely= 0.4, relx = 0.08, anchor = 'center')
	page_4_btn = ctk.CTkButton(window, text= "Page 4", font=(fontype, 16), fg_color= primary_theme, command='')
	page_4_btn.place(rely= 0.5, relx = 0.08, anchor = 'center')
	page_1_frame = ctk.CTkFrame(window, height = 700, width= 800)
	page_1_frame.pack(side='right')
	screenlabel = ctk.CTkLabel(page_1_frame, text= 'PAGE 1', font=(fontype, 50))
	screenlabel.place(rely= 0.5, relx = 0.5, anchor = 'center')
	

def page_2():
	#function to return home page content.
	def switch_to_home():
		page_1_frame.destroy()
		window.update()
		home()
		
	dash_btn = ctk.CTkButton(window, text= "Dashboard", font=(fontype, 16), fg_color= primary_theme, command=switch_to_home)
	dash_btn.place(rely= 0.1, relx = 0.08, anchor = 'center')
	page_1_btn = ctk.CTkButton(window, text= "Page 1", font=(fontype, 16), fg_color= primary_theme, command='')
	page_1_btn.place(rely= 0.2, relx = 0.08, anchor = 'center')
	page_2_btn= ctk.CTkButton(window, text= "Page 2", font=(fontype, 16), fg_color= primary_theme, command='')
	page_2_btn.place(rely= 0.3, relx = 0.08, anchor = 'center')
	page_3_btn = ctk.CTkButton(window, text= "Page 3", font=(fontype, 16), fg_color= primary_theme, command='')
	page_3_btn.place(rely= 0.4, relx = 0.08, anchor = 'center')
	page_4_btn = ctk.CTkButton(window, text= "Page 4", font=(fontype, 16), fg_color= primary_theme, command='')
	page_4_btn.place(rely= 0.5, relx = 0.08, anchor = 'center')
	page_1_frame = ctk.CTkFrame(window, height = 700, width= 800)
	page_1_frame.pack(side='right')
	screenlabel = ctk.CTkLabel(page_1_frame, text= 'PAGE 2', font=(fontype, 50))
	screenlabel.place(rely= 0.5, relx = 0.5, anchor = 'center')
	
	
def page_3():
	#function to return home page content.
	def switch_to_home():
		page_1_frame.destroy()
		window.update()
		home()
		
	dash_btn = ctk.CTkButton(window, text= "Dashboard", font=(fontype, 16), fg_color= primary_theme, command=switch_to_home)
	dash_btn.place(rely= 0.1, relx = 0.08, anchor = 'center')
	page_1_btn = ctk.CTkButton(window, text= "Page 1", font=(fontype, 16), fg_color= primary_theme, command='')
	page_1_btn.place(rely= 0.2, relx = 0.08, anchor = 'center')
	page_2_btn= ctk.CTkButton(window, text= "Page 2", font=(fontype, 16), fg_color= primary_theme, command='')
	page_2_btn.place(rely= 0.3, relx = 0.08, anchor = 'center')
	page_3_btn = ctk.CTkButton(window, text= "Page 3", font=(fontype, 16), fg_color= primary_theme, command='')
	page_3_btn.place(rely= 0.4, relx = 0.08, anchor = 'center')
	page_4_btn = ctk.CTkButton(window, text= "Page 4", font=(fontype, 16), fg_color= primary_theme, command='')
	page_4_btn.place(rely= 0.5, relx = 0.08, anchor = 'center')
	page_1_frame = ctk.CTkFrame(window, height = 700, width= 800)
	page_1_frame.pack(side='right')
	screenlabel = ctk.CTkLabel(page_1_frame, text= 'PAGE 3', font=(fontype, 50))
	screenlabel.place(rely= 0.5, relx = 0.5, anchor = 'center')
	
	
def page_4():
	#function to return home page content.
	def switch_to_home():
		page_1_frame.destroy()
		window.update()
		home()
		
	dash_btn = ctk.CTkButton(window, text= "Dashboard", font=(fontype, 16), fg_color= primary_theme, command=switch_to_home)
	dash_btn.place(rely= 0.1, relx = 0.08, anchor = 'center')
	page_1_btn = ctk.CTkButton(window, text= "Page 1", font=(fontype, 16), fg_color= primary_theme, command='')
	page_1_btn.place(rely= 0.2, relx = 0.08, anchor = 'center')
	page_2_btn= ctk.CTkButton(window, text= "Page 2", font=(fontype, 16), fg_color= primary_theme, command='')
	page_2_btn.place(rely= 0.3, relx = 0.08, anchor = 'center')
	page_3_btn = ctk.CTkButton(window, text= "Page 3", font=(fontype, 16), fg_color= primary_theme, command='')
	page_3_btn.place(rely= 0.4, relx = 0.08, anchor = 'center')
	page_4_btn = ctk.CTkButton(window, text= "Page 4", font=(fontype, 16), fg_color= primary_theme, command='')
	page_4_btn.place(rely= 0.5, relx = 0.08, anchor = 'center')
	page_1_frame = ctk.CTkFrame(window, height = 700, width= 800)
	page_1_frame.pack(side='right')
	screenlabel = ctk.CTkLabel(page_1_frame, text= 'PAGE 4', font=(fontype, 50)) 
	screenlabel.place(rely= 0.5, relx = 0.5, anchor = 'center')
	
home()


window.mainloop()