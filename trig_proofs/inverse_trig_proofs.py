from manim import *
from gtts import gTTS
import os

class InverseTrigProofs(Scene):
    def add_voiceover(self, text, duration=None, file_name="temp_audio.mp3"):
        # Generate TTS audio
        tts = gTTS(text)

        # Make a uniquely named wav file using a random string to avoid caching issues during audio mixing
        import uuid
        unique_name = f"audio_{uuid.uuid4().hex[:8]}.wav"

        import subprocess
        # Save as MP3 first
        tts.save("temp.mp3")
        # Convert directly to WAV using ffmpeg so manim has no issues
        subprocess.run(["ffmpeg", "-y", "-i", "temp.mp3", unique_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Add the audio to the scene
        self.add_sound(unique_name)

        # If no duration is provided, estimate based on words
        if duration is None:
            words = len(text.split())
            duration = max(words * 0.4, 2)  # Estimate 0.4 seconds per word, minimum 2 seconds

        self.wait(duration)

        # We don't remove the file immediately as Manim might need it during rendering
        # It will be overwritten by the next TTS call

    def construct(self):
        self.scene1_introduction()
        self.scene2_question3()
        self.scene3_question4()
        self.scene4_outro()


    def scene1_introduction(self):
        # 0:00 - 0:05
        title = Text("Miscellaneous Exercise: Chapter 2").scale(0.8).move_to(UP)
        subtitle = Text("Inverse Trigonometric Functions").scale(0.6).next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))

        # Audio Voiceover for 0:00 - 0:05
        self.add_voiceover("Welcome back! Today we are diving into the Miscellaneous Exercise for Chapter Two, focusing on inverse trigonometric functions.", duration=4)

        # 0:05 - 0:08
        self.play(FadeOut(title), FadeOut(subtitle))
        self.add_voiceover("We will prove two specific identity problems step-by-step.", duration=3)

    def scene2_question3(self):
        # 0:08 - 0:12
        q3_eq = MathTex(r"2 \sin^{-1}\frac{3}{5} = \tan^{-1}\frac{24}{7}").to_edge(UP)
        self.play(Write(q3_eq))
        self.add_voiceover("Let's start with Question 3. We need to prove that two times inverse sine of three-fifths equals inverse tangent of twenty-four sevenths.", duration=4)

        # 0:12 - 0:18
        # Create a right-angled triangle on the left side of the screen
        triangle = Polygon(
            ORIGIN, RIGHT * 4, RIGHT * 4 + UP * 3,
            color=WHITE
        ).shift(LEFT * 5 + DOWN * 1.5)

        # Adding right angle
        right_angle = RightAngle(
            Line(triangle.get_vertices()[1], triangle.get_vertices()[0]),
            Line(triangle.get_vertices()[1], triangle.get_vertices()[2]),
            length=0.3, quadrant=(1,-1)
        )

        # Adding angle theta
        theta_angle = Angle(
            Line(triangle.get_vertices()[0], triangle.get_vertices()[1]),
            Line(triangle.get_vertices()[0], triangle.get_vertices()[2]),
            radius=0.5
        )
        theta_label = MathTex(r"\theta").next_to(theta_angle, RIGHT, buff=0.1)

        self.play(Create(triangle), Create(right_angle))
        self.play(Create(theta_angle), Write(theta_label))

        self.add_voiceover("Let's look at the left hand side. Let theta equal inverse sine of three-fifths.", duration=4)

        # 0:18 - 0:25
        sin_theta_eq = MathTex(r"\sin \theta = \frac{3}{5}").next_to(triangle, RIGHT, buff=1).shift(UP * 1.5)
        self.play(Write(sin_theta_eq))

        # Labels for opposite and hypotenuse
        opp_label = MathTex("3").next_to(Line(triangle.get_vertices()[1], triangle.get_vertices()[2]), RIGHT)
        hyp_label = MathTex("5").next_to(Line(triangle.get_vertices()[0], triangle.get_vertices()[2]), UL, buff=-0.2)

        self.play(Write(opp_label))
        self.play(Write(hyp_label))

        self.add_voiceover("This means sine of theta is three over five. In our right triangle, the opposite side is three, and the hypotenuse is five.", duration=7)

        # 0:25 - 0:32
        pythagoras = MathTex(r"\text{Base} = \sqrt{5^2 - 3^2} = 4").next_to(triangle, DOWN, buff=0.5)
        self.play(Write(pythagoras))

        adj_label = MathTex("4").next_to(Line(triangle.get_vertices()[0], triangle.get_vertices()[1]), DOWN)
        self.play(Write(adj_label))

        self.add_voiceover("Using the Pythagorean theorem, the base is the square root of five squared minus three squared, which gives us four.", duration=7)

        # 0:32 - 0:40
        tan_theta_eq = MathTex(r"\tan \theta = \frac{3}{4} \Rightarrow \theta = \tan^{-1}\frac{3}{4}").next_to(sin_theta_eq, DOWN, buff=0.5)
        self.play(Write(tan_theta_eq))

        self.add_voiceover("Now we can find tangent of theta, which is opposite over adjacent, or three-fourths. So, theta equals inverse tangent of three-fourths.", duration=8)

        # 0:40 - 0:48
        # Clear triangle area to make room
        self.play(
            FadeOut(triangle), FadeOut(right_angle), FadeOut(theta_angle), FadeOut(theta_label),
            FadeOut(opp_label), FadeOut(hyp_label), FadeOut(adj_label),
            FadeOut(pythagoras), FadeOut(sin_theta_eq), FadeOut(tan_theta_eq)
        )

        new_lhs = MathTex(r"\text{LHS } = 2 \tan^{-1}\frac{3}{4}").move_to(LEFT * 3 + UP * 1.5)
        self.play(Write(new_lhs))

        self.add_voiceover("Substituting this back, our left hand side becomes two times inverse tangent of three-fourths.", duration=5)

        # 0:48 - 0:58
        formula = MathTex(r"2 \tan^{-1}x = \tan^{-1}\frac{2x}{1 - x^2}").move_to(RIGHT * 3).scale(0.8)
        formula_box = SurroundingRectangle(formula, color=YELLOW)
        self.play(Write(formula), Create(formula_box))

        self.add_voiceover("Recall the property for two inverse tangent of x. It equals inverse tangent of two x over one minus x squared.", duration=8)

        # 0:58 - 1:10
        step1 = MathTex(r"= \tan^{-1}\frac{2(3/4)}{1 - (3/4)^2}").next_to(new_lhs, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(step1))
        self.add_voiceover("Plugging in three-fourths for x, we get inverse tangent of two times three-fourths, divided by one minus three-fourths squared.", duration=5)

        step2 = MathTex(r"= \tan^{-1}\frac{3/2}{1 - 9/16}").next_to(step1, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(step2))

        step3 = MathTex(r"= \tan^{-1}\frac{3/2}{7/16}").next_to(step2, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(step3))

        self.add_voiceover("Simplifying the numerator gives three-halves, and the denominator simplifies to seven-sixteenths.", duration=5)

        # 1:10 - 1:15
        final_step = MathTex(r"= \tan^{-1}\left(\frac{3}{2} \cdot \frac{16}{7}\right) = \tan^{-1}\frac{24}{7}").next_to(step3, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(final_step))

        final_box = SurroundingRectangle(final_step, color=GREEN)
        self.play(Create(final_box))

        self.add_voiceover("Multiplying three-halves by sixteen-sevenths gives us twenty-four sevenths. This perfectly matches our Right Hand Side, and the proof is complete.", duration=8)

        # 1:15 - 1:18
        self.play(
            FadeOut(q3_eq), FadeOut(new_lhs), FadeOut(formula), FadeOut(formula_box),
            FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(final_step), FadeOut(final_box)
        )
        self.add_voiceover("Now, let's clear the board for Question 4.", duration=3)

    def scene3_question4(self):
        # 1:18 - 1:24
        q4_eq = MathTex(r"\sin^{-1}\frac{8}{17} + \sin^{-1}\frac{3}{5} =  \tan^{-1}\frac{77}{36}").to_edge(UP)
        self.play(Write(q4_eq))
        self.add_voiceover("For Question 4, we must prove that inverse sine of eight-seventeenths plus inverse sine of three-fifths equals inverse tangent of seventy-seven thirty-sixths.", duration=7)

        # 1:24 - 1:35
        # Split screen setup
        col1_x = LEFT * 3.5
        col2_x = RIGHT * 3.5

        sin_alpha = MathTex(r"\sin \alpha = \frac{8}{17}").move_to(col1_x + UP * 1.5).scale(0.8)
        sin_beta = MathTex(r"\sin \beta = \frac{3}{5}").move_to(col2_x + UP * 1.5).scale(0.8)

        self.play(Write(sin_alpha), Write(sin_beta))
        self.add_voiceover("Since our target is in terms of tangent, let's convert both sine terms into tangent terms. Let the first term be alpha, and the second term be beta.", duration=9)

        # Alpha Triangle (8, 15, 17)
        alpha_tri = Polygon(ORIGIN, RIGHT * 3, RIGHT * 3 + UP * 1.6, color=WHITE).next_to(sin_alpha, DOWN, buff=0.5).scale(0.8)
        a_right_angle = RightAngle(Line(alpha_tri.get_vertices()[1], alpha_tri.get_vertices()[0]), Line(alpha_tri.get_vertices()[1], alpha_tri.get_vertices()[2]), length=0.2, quadrant=(1,-1))
        a_opp_label = MathTex("8").next_to(Line(alpha_tri.get_vertices()[1], alpha_tri.get_vertices()[2]), RIGHT).scale(0.7)
        a_hyp_label = MathTex("17").next_to(Line(alpha_tri.get_vertices()[0], alpha_tri.get_vertices()[2]), UL, buff=-0.1).scale(0.7)

        self.play(Create(alpha_tri), Create(a_right_angle))
        self.play(Write(a_opp_label), Write(a_hyp_label))

        # 1:35 - 1:45
        tan_alpha_step1 = MathTex(r"\text{Base} = \sqrt{17^2 - 8^2} = 15").next_to(alpha_tri, DOWN, buff=0.2).scale(0.7)
        a_adj_label = MathTex("15").next_to(Line(alpha_tri.get_vertices()[0], alpha_tri.get_vertices()[1]), DOWN).scale(0.7)

        tan_alpha_step2 = MathTex(r"\tan \alpha = \frac{8}{15} \Rightarrow \alpha = \tan^{-1}\frac{8}{15}").next_to(tan_alpha_step1, DOWN, buff=0.3).scale(0.7)

        self.play(Write(tan_alpha_step1), Write(a_adj_label))
        self.play(Write(tan_alpha_step2))
        self.add_voiceover("For alpha, the opposite is eight and hypotenuse is seventeen. Using Pythagoras, the base is fifteen. So, alpha equals inverse tangent of eight-fifteenths.", duration=10)

        # Beta Triangle (3, 4, 5)
        beta_tri = Polygon(ORIGIN, RIGHT * 2.5, RIGHT * 2.5 + UP * 1.875, color=WHITE).next_to(sin_beta, DOWN, buff=0.5).scale(0.8)
        b_right_angle = RightAngle(Line(beta_tri.get_vertices()[1], beta_tri.get_vertices()[0]), Line(beta_tri.get_vertices()[1], beta_tri.get_vertices()[2]), length=0.2, quadrant=(1,-1))
        b_opp_label = MathTex("3").next_to(Line(beta_tri.get_vertices()[1], beta_tri.get_vertices()[2]), RIGHT).scale(0.7)
        b_hyp_label = MathTex("5").next_to(Line(beta_tri.get_vertices()[0], beta_tri.get_vertices()[2]), UL, buff=-0.1).scale(0.7)

        self.play(Create(beta_tri), Create(b_right_angle))
        self.play(Write(b_opp_label), Write(b_hyp_label))

        # 1:45 - 1:52
        tan_beta_step1 = MathTex(r"\text{Base} = \sqrt{5^2 - 3^2} = 4").next_to(beta_tri, DOWN, buff=0.2).scale(0.7)
        b_adj_label = MathTex("4").next_to(Line(beta_tri.get_vertices()[0], beta_tri.get_vertices()[1]), DOWN).scale(0.7)

        tan_beta_step2 = MathTex(r"\tan \beta = \frac{3}{4} \Rightarrow \beta = \tan^{-1}\frac{3}{4}").next_to(tan_beta_step1, DOWN, buff=0.3).scale(0.7)

        self.play(Write(tan_beta_step1), Write(b_adj_label))
        self.play(Write(tan_beta_step2))
        self.add_voiceover("For beta, we already know a three-four-five triangle. The base is four, so beta equals inverse tangent of three-fourths.", duration=7)

        # 1:52 - 2:00
        self.play(
            FadeOut(sin_alpha), FadeOut(sin_beta),
            FadeOut(tan_alpha_step1), FadeOut(tan_beta_step1),
            FadeOut(tan_alpha_step2), FadeOut(tan_beta_step2),
            FadeOut(alpha_tri), FadeOut(a_right_angle), FadeOut(a_opp_label), FadeOut(a_hyp_label), FadeOut(a_adj_label),
            FadeOut(beta_tri), FadeOut(b_right_angle), FadeOut(b_opp_label), FadeOut(b_hyp_label), FadeOut(b_adj_label)
        )

        new_lhs = MathTex(r"\text{LHS } = \tan^{-1}\frac{8}{15} + \tan^{-1}\frac{3}{4}").move_to(LEFT * 2 + UP * 1)
        self.play(Write(new_lhs))
        self.add_voiceover("Now, rewrite our left hand side with our new tangent values.", duration=5)

        # 2:00 - 2:08
        formula = MathTex(r"\tan^{-1}x + \tan^{-1}y = \tan^{-1}\frac{x + y}{1 - xy}").move_to(RIGHT * 2 + UP * 1).scale(0.8)
        formula_box = SurroundingRectangle(formula, color=YELLOW)
        self.play(Write(formula), Create(formula_box))
        self.add_voiceover("We can use the inverse tangent addition formula: inverse tangent of x plus y, over one minus x times y.", duration=8)

        # 2:08 - 2:20
        step1 = MathTex(r"= \tan^{-1}\frac{8/15 + 3/4}{1 - (8/15)(3/4)}").next_to(new_lhs, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(step1))
        self.add_voiceover("Substitute eight-fifteenths for x and three-fourths for y.", duration=4)

        step2 = MathTex(r"= \tan^{-1}\frac{(32 + 45)/60}{1 - 24/60}").next_to(step1, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(step2))
        self.add_voiceover("In the numerator, finding a common denominator of sixty gives us thirty-two plus forty-five. In the denominator, we get one minus twenty-four sixtieths.", duration=9)

        # 2:20 - 2:28
        # Step 3 part A: showing the fractions
        step3_pt1 = MathTex(r"= \tan^{-1}\frac{77/60}{36/60}").next_to(step2, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(step3_pt1))

        # Animate the cancellation of the 60s
        # Approximate positions of the "60"s relative to the MathTex
        cross_up = Line(step3_pt1.get_center() + UP*0.1 + LEFT*0.1, step3_pt1.get_center() + UP*0.3 + RIGHT*0.15, color=RED)
        cross_down = Line(step3_pt1.get_center() + DOWN*0.3 + LEFT*0.1, step3_pt1.get_center() + DOWN*0.1 + RIGHT*0.15, color=RED)
        self.play(Create(cross_up), Create(cross_down))

        # Step 3 part B: showing the final answer
        step3_pt2 = MathTex(r"= \tan^{-1}\frac{77}{36}").next_to(step3_pt1, RIGHT, buff=0.2)
        self.play(Write(step3_pt2))

        final_box = SurroundingRectangle(step3_pt2, color=GREEN)
        self.play(Create(final_box))
        self.add_voiceover("This simplifies to seventy-seven sixtieths divided by thirty-six sixtieths. The sixtieths cancel out, leaving us with inverse tangent of seventy-seven thirty-sixths. The right hand side is proved!", duration=10)

        # Transition to outro
        self.play(
            FadeOut(q4_eq), FadeOut(new_lhs), FadeOut(formula), FadeOut(formula_box),
            FadeOut(step1), FadeOut(step2), FadeOut(step3_pt1), FadeOut(cross_up), FadeOut(cross_down), FadeOut(step3_pt2), FadeOut(final_box)
        )

    def scene4_outro(self):

        # 2:28 - 2:35
        thanks_text = Text("Thanks for watching!").scale(1.2).move_to(ORIGIN)

        # Simple geometric shapes/sine wave animating in background
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            y_length=3,
            axis_config={"color": BLUE},
        ).set_opacity(0.3)
        sine_wave = axes.plot(lambda x: np.sin(x), color=YELLOW).set_opacity(0.3)

        self.play(Write(thanks_text))
        self.play(Create(axes), Create(sine_wave))

        self.add_voiceover("And that wraps up both proofs! Converting to inverse tangent is often the most straightforward path for these identities. Thanks for watching, and keep practicing!", duration=10)

        self.wait(2)
        self.play(FadeOut(thanks_text), FadeOut(axes), FadeOut(sine_wave))

if __name__ == "__main__":
    # Useful for testing directly
    pass
