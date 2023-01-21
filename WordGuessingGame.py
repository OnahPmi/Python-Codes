#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def word_guessing_game():
#     from IPython.display import display, Markdown, Latex
    print(""" 
######################################################################################################
#    This is a word guessing game. Users are given 3 chances to guess three secret words correctly.  #
#                   The three words must be given as one entry seperated by commas.                  # 
#                                                                                                    #
#                                       **Break a leg!**                                             #
#                                                                                                    #
#        *Hint: Secret words are words that show courage, lack of courage and no perspective.*       #
######################################################################################################
""")
    counter=1
    secret_words = ["brave", "coward", "indifference"] # Defining the secret words

    secret_word1, secret_word2, secret_word3 = secret_words

    while counter <= 3:
        try:
            user_guesses = input("Please input your guesses separated by commas: ").lower().strip(" ,.;:")
            guess_list = user_guesses.split(",")
#             print(f"splitted string = {guess_list}")
            new_guess_list = []
            for item in guess_list:
                if len(item) != 0:
                    new_guess_list.append(item.strip(" ,.;:"))

            guess1, guess2, guess3 = new_guess_list # Unpack the numbers into separate variables
            print(f"""
                    #################################################################
                       Your entries are: {guess1}, {guess2}, and {guess3}""") 
            
            condition1 = secret_word1 in new_guess_list and secret_word2 in new_guess_list
            condition2 = secret_word1 in new_guess_list and secret_word3 in new_guess_list
            condition3 = secret_word2 in new_guess_list and secret_word3 in new_guess_list
            
            if secret_word1 in new_guess_list and secret_word2 in new_guess_list and secret_word3 in new_guess_list:
                print(f"""
                       You won 😊😊!
                       Score = {len(secret_words)*100/len(secret_words):.2f}%
                    ##################################################################
                    """)
                break
                
            elif condition1 or condition2 or condition3:
                if counter < 3:
                    print(f"""
                       You got {len(new_guess_list)-1} words correctly.            
                       Score = {(len(secret_words)-1)*100/len(secret_words):.2f}%  
                       Try again! You have {3-counter} chance(s) left              
                    ################################################################""")
                    counter+=1
                elif counter==3:
                    print(f"""
                       Score = {(len(secret_words)-1)*100/len(secret_words):.2f}%                        
                       Final remark: Good 😊!                                                           
                       You have exhausted your chances for this round! 
                       If you are on the Command Line or Terminal, Reload the Script to Try again
                       If you are on Google Colab or Jupyter-Notebook, Click Ctrl + Enter to try again!  
                    ######################################################################################""")
                    break
                    
            elif secret_word1 in new_guess_list or secret_word2 in new_guess_list or secret_word3 in new_guess_list:
                if counter < 3:
                    print(f"""
                       You got {len(new_guess_list)-2} words correctly.            
                       Score = {(len(secret_words)-2)*100/len(secret_words):.2f}%  
                       Try again! You have {3-counter} chance(s) left              
                    #################################################################""")
                    counter+=1
                elif counter==3:
                    print(f"""
                       Score = {(len(secret_words)-2)*100/len(secret_words):.2f}%                       
                       Final remark: Poor 😔😔!                                                        
                       You have exhausted your chances for this round! 
                       If you are on the Command Line or Terminal, Reload the Script to Try again
                       If you are on Google Colab or Jupyter-Notebook, Click Ctrl + Enter to try again! 
                    ######################################################################################""")
                    break
            else:
                if counter < 3:
                    print(f"""
                       You got {len(new_guess_list)-3} words correctly.            
                       Score = {(len(secret_words)-3)*100/len(secret_words):.2f}%  
                       Try again! You have {3-counter} chance(s) left              
                    #################################################################""")
                    counter+=1
                elif counter==3:
                    print(f"""
                       Score = {(len(secret_words)-3)*100/len(secret_words):.2f}%                        
                       Final remark: Failed 😔😔!                                                       
                       You have exhausted your chances for this round! 
                       If you are on the Command Line or Terminal, Reload the Script to Try again
                       If you are on Google Colab or Jupyter-Notebook, Click Ctrl + Enter to try again!  
                    ######################################################################################""")
                    break
                    
        except ValueError:
            print(f"""
            Number of words must be equal to 3, but {len(new_guess_list)} was given.\n
            You have {3-counter} chance(s) left 
            """)
            counter+=1
    else:
        print(f"""
            Score = {(len(secret_words)-3)*100/len(secret_words):.2f}%                        
            Final remark: Failed 😔😔!                                                       
            You have exhausted your chances for this round! 
            If you are on the Command Line or Terminal, Reload the Script to Try again
            If you are on Google Colab or Jupyter-Notebook, Click Ctrl + Enter to try again!   
         ######################################################################################""")
            
word_guessing_game()

