from experta import *

class Environment(Fact):
    """Represents the environment a trainee interacts with."""
    pass

class Job(Fact):
    """Represents the job type for the trainee."""
    pass


class Feedback(Fact):
    """Indicates whether feedback is required."""
    pass

class Medium(Fact):
    """Represents the medium selected based on rules."""
    pass

class MediaAdvisor(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        print("Initializing the Media Advisor Expert System...\n")
# Rule 1
    @Rule(Environment(environment='papers') |
          Environment(environment='manuals') |
          Environment(environment='documents') |
          Environment(environment='textbooks'))
    def verbal(self):
        print("Rule triggered: Environment is 'verbal'.")
        self.declare(Fact(stimulus_situation='verbal'))

# Rule 2
    @Rule(Environment(environment='pictures') |
          Environment(environment='illustrations') |
          Environment(environment='photographs') |
          Environment(environment='diagrams'))
    def visual(self):
        print("Rule triggered: Environment is 'visual'.")
        self.declare(Fact(stimulus_situation='visual'))
# Rule 3
    @Rule(Environment(environment='machines') |
          Environment(environment='buildings') |
          Environment(environment='tools'))
    def physical_object(self):
        print("Rule triggered: Environment is a 'physical object'.")
        self.declare(Fact(stimulus_situation='physical object'))
# Rule 4
    @Rule(Environment(environment='numbers') |
          Environment(environment='formulas') |
          Environment(environment='computer programs'))
    def symbolic(self):
        print("Rule triggered: Environment is 'symbolic'.")
        self.declare(Fact(stimulus_situation='symbolic'))
# Rule 5
    @Rule(Job(job='lecturing') |
          Job(job='advising') |
          Job(job='counselling'))
    def oral_response(self):
        print("Rule triggered: Job requires 'oral' response.")
        self.declare(Fact(stimulus_response='oral'))
# Rule 6
    @Rule(Job(job='building') |
          Job(job='repairing') |
          Job(job='troubleshooting'))
    def hands_on(self):
        print("Rule triggered: Job requires 'hands-on' response.")
        self.declare(Fact(stimulus_response='hands-on'))
# Rule 7
    @Rule(Job(job='writing') |
          Job(job='typing') |
          Job(job='drawing'))
    def documented_response(self):
        print("Rule triggered: Job requires 'documented' response.")
        self.declare(Fact(stimulus_response='documented'))
# Rule 8
    @Rule(Job(job='evaluating') |
          Job(job='reasoning') |
          Job(job='investigating'))
    def analytical_response(self):
        print("Rule triggered: Job requires 'analytical' response.")
        self.declare(Fact(stimulus_response='analytical'))
# Rule 9
    @Rule(Fact(stimulus_situation='physical object'),
          Fact(stimulus_response='hands-on'),
          Feedback(feedback='required'))
    def workshop(self):
        print("Final Rule triggered: Selecting medium 'Workshop'.")
        self.declare(Medium(medium='workshop'))
        print("Recommended Medium: Workshop\n")
# Rule 10
    @Rule(Fact(stimulus_situation='symbolic'),
          Fact(stimulus_response='analytical'),
          Feedback(feedback='required'),salience = 2) # Higher priority
    def lecture_tutorial_symbolic(self):
        print("Final Rule triggered: Selecting medium 'Lecture - Tutorial' for symbolic environment.")
        self.declare(Medium(medium='lecture - tutorial'))
        print("Recommended Medium: Lecture - Tutorial\n")
# Rule 11
    @Rule(Fact(stimulus_situation='visual'),
          Fact(stimulus_response='documented'),
          Feedback(feedback='required'))
    def videocassette(self):
        print("Final Rule triggered: Selecting medium 'Videocassette'.")
        self.declare(Medium(medium='videocassette'))
        print("Recommended Medium: Videocassette\n")
# Rule 12
    @Rule(Fact(stimulus_situation='verbal'),
          Fact(stimulus_response='analytical'),
          Feedback(feedback='required'),salience = 1) # Lower priority
    def lecture_tutorial_verbal(self):
        print("Final Rule triggered: Selecting medium 'Lecture - Tutorial' for verbal environment.")
        self.declare(Medium(medium='lecture - tutorial'))
        print("Recommended Medium: Lecture - Tutorial\n")

advisor = MediaAdvisor()
print("Conflict Scenario Test:")
advisor.reset()

print("Test Case 1:") # دمج environment مع بعض 
advisor.declare(Environment(environment='formulas'))
advisor.declare(Environment(environment='documents'))
advisor.declare(Job(job='reasoning'))
advisor.declare(Feedback(feedback='required'))
advisor.run()

print("_"*40)
print("Test Case 2:")
advisor.reset()
advisor.declare(Environment(environment='formulas'))
advisor.declare(Job(job='reasoning'))
advisor.declare(Feedback(feedback='required'))
advisor.run()

print("_"*40)
print("Test Case 3:")
advisor.reset()
advisor.declare(Environment(environment='textbooks'))
advisor.declare(Job(job='reasoning'))
advisor.declare(Feedback(feedback='required'))
advisor.run()

