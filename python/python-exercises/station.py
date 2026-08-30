def play_game(player):
    # Chapter 1 Meet the Monkey King -- Wukong
    print("Meet the Monkey King")
    story_text1 = "Master. Xuanzang passes by Hand Mountain and hears a desperate voice trapped beneath the heavy rocks."
    story_text2 = "Goddess Guanyin appears and says: 'This is Wukong, former Monkey King. He was punished by the Buddha for his arrogance and aggression. Now it is time for him to start a new life. Take him as your first companion, but be careful of his temper.'"
    print(story_text1)
    print(story_text2)

    talk = input("Talk to Wukong? (Enter 'Yes' or 'No'): ")
    if talk == "Yes":
        Wukong_intro = input("Wukong shouts: 'I will break free and go back to my home mountain! What do you want from me, you the bald': ")
        print(Wukong_intro)

        print("How do you respond to Wukog?")
        print("A = Sit down, listen to his 500-year solitude, clean his fur and share your food and mission, kindly invite him as an equal partner")
        print("B = Feed him fruits and offer a practical deal: freedom in exchange for protection")
        print("C = Recite the tightening curse to force his submission and bring up his past mistakes")
        
        opt_WK = input("Enter A, B, or C: ")
        if opt_WK == "A":
            print("Trust score + 20!")
            player.trust_score += 20
            player.team.append("Wukong")
        elif opt_WK == "B":
            print("Trust score + 10!")
            player.trust_score += 10
            player.team.append("Wukong")
        elif opt_WK == "C":
            print("Trust score + 0!")
            player.trust_score += 0
            player.team.append("Wukong")
        else:
            print("Please choose again!")
    else:
        print("Let's hiking for a while!")

    # Chapter 2 Meet Pigsy -- Bajay (The Ex-god from Heaven)
    print("Meet Pigsy, Bajay")
    story_text1 = "Xuanzang and Wukong arrive at Gao Village. The villagers complain about a monster with a pig-like face who has taken over a household and ruined the farmland."
    story_text2 = "They find out he was once a god from Heaven, exiled to human world for misbehavior. Despite his terrifying appearance, he has a soft heart and is loyal to people he loves."
    print(story_text1)
    print(story_text2)
        
    Bajay_intro = input("Pigsy grumbles: 'Everyone judges me by my looks! I just want a peaceful life and full meals.'")
    print(Bajay_intro)
    talk = input("Talk to Pigsy? (Enter 'Yes' or 'No'): ")
    if talk == "Yes":
        print("How do you respond to Pigsy?")
        print("A = Show respect for his historic honor, show empathy to his experience, and invite him to seek a greater destiny with you (+20 Trust)")
        print("B = Offer him a practical contract: full meals through the journey and permanent position in Heaven's official department after the journey (+10 Trust)")
        print("C = Let Wukong threaten him with the weapon and forbid him from seeking a family (-10 Trust)")
            
        opt_BJ = input("Enter A, B, or C: ")
        
        if opt_BJ == "A":
            print("Trust score + 20!")
            player.trust_score += 20
            player.team.append("Bajay")
        elif opt_BJ == "B":
            print("Trust score + 10!")
            player.trust_score += 10
            player.team.append("Bajay")
        elif opt_BJ == "C":
            print("Trust score + 0")
            player.trust_score += 0
            player.team.append("Bajay")
        else:
            print("Invalid choice! No trust change.")
    else:
        print("You bypassed Gao Village without talking to Pigsy.")

    # Chapter 3: The Riverside Monster -- Sandy
    print("Chapter 3: The Riverside Monster Sandy")
    story_text1 = "The team arrives at the scary Flowing Sands River. A fierce, red-bearded river monster emerges from the deep waters."
    story_text2 = "Bajay reveals that he was once the General of the Guard team. He was exiled for breaking a valuable crystal and today suffers daily torture from flying swords."
        
    print(story_text1)
    print(story_text2)
        
    talk = input("Talk to Sandy? (Enter 'Yes' or 'No') ")
        
    if talk == "Yes":
        print("Sandy speaks with deep shame and anxiety: 'I am a sinner trapped in endless punishment. Why would you want me?'")
        print("How do you respond to Sandy?")
        print("A = Provide emotional safety, tell him he is no longer a sinner in your team, and value him as a key partner in this great journey (+20 Trust)")
        print("B = Assign him a clear task: look after the luggage and logistics, promising to free him from the river (+10 Trust)")
        print("C = Preach to him sternly that he must endure all hardship during the journey to redeem his heavy sins (-10 Trust)")
            
        opt_SD = input("Enter A, B, or C: ")
        if opt_SD == "A":
            print("Trust score + 20!")
            player.trust_score += 20
            player.team.append("Sandy")
        elif opt_SD == "B":
            print("Trust score + 10!")
            player.trust_score += 10
            player.team.append("Sandy")
        elif opt_SD == "C":
            print("Trust score + 0!")
            player.trust_score += 0
            player.team.append("Sandy")
        else:
            print("Invalid choice! No trust change.")
    else:
        print("You decided not to speak with Sandy.")

    # Final Evaluation
    print("Final Evaluation & Game Ending")
    print(f"Final Trust Score: {player.trust_score}")
    print(f"Final Team: {player.team}")

    final_words = ""
    if player.trust_score >= 60:
        final_words = "Ending 1: Best Partnership - The team start their journey as true, trusted and equal companions."
    elif player.trust_score >= 40:
        final_words = "Ending 2: Good Cooperation - The team functions like a professional group in the begining."
    else:
        final_words = "Ending 3: Forced Alliance - The team walk into the journey under tension and mistrust."
            
    print(f"{final_words}")