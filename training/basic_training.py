"""
Basic Training Module for the Cognitive Fortress Framework.
"""

class TrainingModule:
    """
    Base class for training modules in the Cognitive Fortress Framework.
    """
    
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.lessons = []
        self.exercises = []
        
    def add_lesson(self, title, content):
        """Add a lesson to the training module."""
        lesson = {
            "title": title,
            "content": content,
            "exercises": []
        }
        self.lessons.append(lesson)
        
    def add_exercise(self, lesson_index, exercise):
        """Add an exercise to a specific lesson."""
        if 0 <= lesson_index < len(self.lessons):
            self.lessons[lesson_index]["exercises"].append(exercise)
            
    def start_training(self):
        """Start the training session."""
        print(f"Starting training: {self.name}")
        print(f"Description: {self.description}")
        
        for i, lesson in enumerate(self.lessons):
            print(f"\nLesson {i+1}: {lesson['title']}")
            print(lesson['content'])
            
            if lesson['exercises']:
                print("\nExercises:")
                for j, exercise in enumerate(lesson['exercises']):
                    print(f"  Exercise {j+1}: {exercise}")


class CognitiveDefenseBasics(TrainingModule):
    """
    Basic training module covering fundamental cognitive defense concepts.
    """
    
    def __init__(self):
        super().__init__(
            name="Cognitive Defense Basics",
            description="Learn the fundamentals of cognitive defense and protection against manipulation."
        )
        
        # Add lessons
        self.add_lesson(
            "Introduction to Cognitive Defense",
            """
Cognitive defense involves protecting your thought processes from manipulation and bias.
This includes recognizing manipulation tactics, understanding cognitive biases, and developing
critical thinking skills.
            """
        )
        
        self.add_lesson(
            "Common Manipulation Tactics",
            """
Common manipulation tactics include:
- Emotional appeals and fear mongering
- Authority bias exploitation
- Social proof manipulation
- Scarcity and urgency creation
- Reciprocity pressure
            """
        )
        
        self.add_lesson(
            "Critical Thinking Techniques",
            """
Effective critical thinking techniques include:
- Questioning assumptions
- Evaluating evidence quality
- Considering alternative explanations
- Checking logical consistency
- Identifying potential biases
            """
        )
        
        # Add exercises to lessons
        self.add_exercise(0, "Reflect on a recent situation where you felt pressured to make a decision.")
        self.add_exercise(1, "Identify manipulation tactics in news headlines or advertisements.")
        self.add_exercise(2, "Practice questioning assumptions in a statement you agree with.")


def run_sample_training():
    """Run a sample training session."""
    training = CognitiveDefenseBasics()
    training.start_training()


if __name__ == "__main__":
    run_sample_training()