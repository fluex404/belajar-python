from random import randint


def main():
    words = """
            Above 	Alike 	Arise 	Began
            Abuse 	Alive 	Array 	Begin
            Actor 	Allow 	Aside 	Begun
            Acute 	Alone 	Asset 	Being
            Admit 	Along 	Audio 	Below
            Adopt 	Alter 	Audit 	Bench
            Adult 	Among 	Avoid 	Billy
            After 	Anger 	Award 	Birth
            Again 	Angle 	Aware 	Black
            Agent 	Angry 	Badly 	Blame
            Agree 	Apart 	Baker 	Blind
            Ahead 	Apple 	Bases 	Block
            Alarm 	Apply 	Basic 	Blood
            Album 	Arena 	Basis 	Board
            Boost 	Buyer 	China 	Cover
            Booth 	Cable 	Chose 	Craft
            Bound 	Calif 	Civil 	Crash
            Brain 	Carry 	Claim 	Cream
            Brand 	Catch 	Class 	Crime
            Bread 	Cause 	Clean 	Cross
            Break 	Chain 	Clear 	Crowd
            Breed 	Chair 	Click 	Crown
            Brief 	Chart 	Clock 	Curve
            Bring 	Chase 	Close 	Cycle
            Broad 	Cheap 	Coach 	Daily
            Broke 	Check 	Coast 	Dance
            Brown 	Chest 	Could 	Dated
            Build 	Chief 	Count 	Dealt
            Built 	Child 	Court 	Death
            Debut 	Entry 	Forth 	Group
            Delay 	Equal 	Forty 	Grown
            Depth 	Error 	Forum 	Guard
            Doing 	Event 	Found 	Guess
            Doubt 	Every 	Frame 	Guest
            Dozen 	Exact 	Frank 	Guide
            Draft 	Exist 	Fraud 	Happy
            Drama 	Extra 	Fresh 	Harry
            Drawn 	Faith 	Front 	Heart
            Dream 	False 	Fruit 	Heavy
            Dress 	Fault 	Fully 	Hence
            Drill 	Fiber 	Funny 	Night
            Drink 	Field 	Giant 	Horse
            Drive 	Fifth 	Given 	Hotel
            Drove 	Fifty 	Glass 	House
            Dying 	Fight 	Globe 	Human
            Eager 	Final 	Going 	Ideal
            Early 	First 	Grace 	Image
            Earth 	Fixed 	Grade 	Index
            Eight 	Flash 	Grand 	Inner
            Elite 	Fleet 	Grant 	Input
            Empty 	Floor 	Grass 	Issue
            Enemy 	Fluid 	Great 	Irony
            Enjoy 	Focus 	Green 	Juice
            Enter 	Force 	Gross 	Joint
            Judge 	Metal 	Media 	Newly
            Known 	Local 	Might 	Noise
            Label 	Logic 	Minor 	North
            Large 	Loose 	Minus 	Noted
            Laser 	Lower 	Mixed 	Novel
            Later 	Lucky 	Model 	Nurse
            Laugh 	Lunch 	Money 	Occur
            Layer 	Lying 	Month 	Ocean
            Learn 	Magic 	Moral 	Offer
            Lease 	Major 	Motor 	Often
            Least 	Maker 	Mount 	Order
            Leave 	March 	Mouse 	Other
            Legal 	Music 	Mouth 	Ought
            Level 	Match 	Movie 	Paint
            Light 	Mayor 	Needs 	Paper
            Limit 	Meant 	Never 	Party
            Peace 	Power 	Radio 	Round
            Panel 	Press 	Raise 	Route
            Phase 	Price 	Range 	Royal
            Phone 	Pride 	Rapid 	Rural
            Photo 	Prime 	Ratio 	Scale
            Piece 	Print 	Reach 	Scene
            Pilot 	Prior 	Ready 	Scope
            Pitch 	Prize 	Refer 	Score
            Place 	Proof 	Right 	Sense
            Plain 	Proud 	Rival 	Serve
            Plane 	Prove 	River 	Seven
            Plant 	Queen 	Quick 	Shall
            Plate 	Sixth 	Stand 	Shape
            Point 	Quiet 	Roman 	Share
            Pound 	Quite 	Rough 	Sharp
            Sheet 	Spare 	Style 	Times
            Shelf 	Speak 	Sugar 	Tired
            Shell 	Speed 	Suite 	Title
            Shift 	Spend 	Super 	Today
            Shirt 	Spent 	Sweet 	Topic
            Shock 	Split 	Table 	Total
            Shoot 	Spoke 	Taken 	Touch
            Short 	Sport 	Taste 	Tough
            Shown 	Staff 	Taxes 	Tower
            Sight 	Stage 	Teach 	Track
            Since 	Stake 	Teeth 	Trade
            Sixty 	Start 	Texas 	Treat
            Sized 	State 	Thank 	Trend
            Skill 	Steam 	Theft 	Trial
            Sleep 	Steel 	Their 	Tried
            Slide 	Stick 	Theme 	Tries
            Small 	Still 	There 	Truck
            Smart 	Stock 	These 	Truly
            Smile 	Stone 	Thick 	Trust
            Smith 	Stood 	Thing 	Truth
            Smoke 	Store 	Think 	Twice
            Solid 	Storm 	Third 	Under
            Solve 	Story 	Those 	Undue
            Sorry 	Strip 	Three 	Union
            Sound 	Stuck 	Threw 	Unity
            South 	Study 	Throw 	Until
            Space 	Stuff 	Tight 	Upper
            Upset 	Whole 	Waste 	Wound
            Urban 	Whose 	Watch 	Write
            Usage 	Woman 	Water 	Wrong
            Usual 	Train 	Wheel 	Wrote
            Valid 	World 	Where 	Yield
            Value 	Worry 	Which 	Young
            Video 	Worse 	While 	Youth
            Virus 	Worst 	White 	Worth
            Visit 	Would 	Vital 	Voice
            """.lower().split()

    chosen_word = words[randint(0, len(words))]
    guess_status = [False, False, False, False, False]

    print("welkam to mai wordel gem")

    for triesLeft in range(6, 0, -1):
        print(f"{triesLeft} tries left")

        guess = input("\nPlis ges -> ")

        print("".join(match_comparison(char, i, chosen_word) for (i, char) in enumerate(guess)))

        for i, char in enumerate(guess):
            if chosen_word[i] == char:
                guess_status[i] = True

            if all(guess_status):
                print("waw yu win")
                return

    print("HAHA YU LUSSS")
    print(f"Answer: {chosen_word}")


def match_comparison(char: str, i: int, chosen_word: str) -> str:
    if char == chosen_word[i]:
        return "V"
    if char in


if __name__ == "__main__":
    main()
