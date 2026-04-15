from manim import *
import numpy as np

class Scene7(Scene):
    def construct(self):
        # van't Hoff Factor (i) for NaCl
        title = Text("van't Hoff Factor (i)", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Beaker
        beaker = VGroup(
            Line(LEFT*2, RIGHT*2),
            Line(LEFT*2, LEFT*2 + UP*3),
            Line(RIGHT*2, RIGHT*2 + UP*3)
        ).move_to(DOWN*1)
        water = Rectangle(width=3.9, height=2.5, color=BLUE, fill_opacity=0.3).move_to(DOWN*0.75)

        self.play(Create(beaker), FadeIn(water))

        # NaCl Crystal
        crystal = VGroup()
        for i in range(2):
            for j in range(2):
                color = GREEN if (i+j)%2 == 0 else PURPLE
                crystal.add(Circle(radius=0.3, color=color, fill_opacity=1).move_to(LEFT*(i-0.5)*0.6 + UP*(j-0.5)*0.6))
        crystal.move_to(UP*3)

        crystal_label = Text("NaCl Crystal", font_size=20).next_to(crystal, UP)

        self.play(FadeIn(crystal), Write(crystal_label))

        # Trackers
        theo_text = Text("Theoretical Particles Added: 1 Formula Unit", font_size=24).to_edge(LEFT).shift(UP*1)
        obs_text = Text("Actual Particles in Solution: 0 Ions", font_size=24).to_edge(LEFT).shift(UP*0)

        self.play(Write(theo_text))
        self.play(Write(obs_text))

        # Drop and break
        self.play(crystal.animate.move_to(DOWN*0.5), FadeOut(crystal_label), run_time=2)

        # Scatter
        na_ion1 = crystal[0].animate.move_to(LEFT*1 + DOWN*0.2)
        cl_ion1 = crystal[1].animate.move_to(RIGHT*0.5 + UP*0.2)
        na_ion2 = crystal[3].animate.move_to(RIGHT*1 + DOWN*1)
        cl_ion2 = crystal[2].animate.move_to(LEFT*0.5 + DOWN*1.5)

        self.play(na_ion1, cl_ion1, na_ion2, cl_ion2)

        obs_text_new = Text("Actual Particles in Solution: 2 Ions (per unit)", font_size=24).to_edge(LEFT).shift(UP*0)
        self.play(Transform(obs_text, obs_text_new))

        # Formula
        form1 = MathTex("i = \\frac{\\text{Observed Particles}}{\\text{Theoretical Particles}}", font_size=36).move_to(RIGHT*2 + UP*1)
        form2 = MathTex("i = \\frac{2}{1} = 2", font_size=40, color=YELLOW).move_to(RIGHT*2 + DOWN*0.5)

        self.play(Write(form1))
        self.wait(1)
        self.play(Write(form2))
        self.wait(6)


class Scene8(Scene):
    def construct(self):
        # Freezing Point Depression
        title = Text("Freezing Point Depression", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Split screen
        line = Line(UP*3, DOWN*3)
        self.play(Create(line))

        # Left: Sugar
        s_title = Text("5% Cane Sugar", font_size=30).move_to(LEFT*3 + UP*2)
        s_mass = Text("(342 g/mol)", font_size=20).next_to(s_title, DOWN)

        # Sugar molecules (complex)
        s_mols = VGroup(*[Circle(radius=0.3, color=RED, fill_opacity=0.5).move_to(LEFT*(2+np.random.rand()*2) + UP*(np.random.rand()*2-1)) for _ in range(5)])

        s_therm_rect = Rectangle(width=0.4, height=3, color=WHITE).move_to(LEFT*3 + DOWN*1.5)
        s_therm_bulb = Circle(radius=0.4, color=RED, fill_opacity=1).next_to(s_therm_rect, DOWN, buff=-0.1)
        s_therm_liquid = Rectangle(width=0.3, height=2.5, color=RED, fill_opacity=1).move_to(s_therm_rect.get_bottom() + UP*1.25)
        s_therm = VGroup(s_therm_rect, s_therm_bulb, s_therm_liquid)

        s_temp = Text("271 K", font_size=24).next_to(s_therm, LEFT)

        self.play(Write(s_title), Write(s_mass), FadeIn(s_mols), Create(s_therm), Write(s_temp))

        # Right: Glucose
        g_title = Text("5% Glucose", font_size=30).move_to(RIGHT*3 + UP*2)
        g_mass = Text("(180 g/mol)", font_size=20).next_to(g_title, DOWN)

        # Glucose molecules (smaller, more numerous)
        g_mols = VGroup(*[Circle(radius=0.15, color=GREEN, fill_opacity=0.5).move_to(RIGHT*(2+np.random.rand()*2) + UP*(np.random.rand()*2-1)) for _ in range(10)])

        g_therm_rect = Rectangle(width=0.4, height=3, color=WHITE).move_to(RIGHT*3 + DOWN*1.5)
        g_therm_bulb = Circle(radius=0.4, color=RED, fill_opacity=1).next_to(g_therm_rect, DOWN, buff=-0.1)
        g_therm_liquid = Rectangle(width=0.3, height=2.5, color=RED, fill_opacity=1).move_to(g_therm_rect.get_bottom() + UP*1.25)
        g_therm = VGroup(g_therm_rect, g_therm_bulb, g_therm_liquid)

        g_temp = Text("273 K", font_size=24).next_to(g_therm, RIGHT)

        self.play(Write(g_title), Write(g_mass), FadeIn(g_mols), Create(g_therm), Write(g_temp))

        # Formula and calculation
        form = MathTex("\\Delta T_f = K_f \\cdot m", font_size=36).move_to(UP*2)
        calc_text = Text("Lower molar mass = More moles = More particles", font_size=24, color=YELLOW).move_to(UP*1)

        self.play(Write(form))
        self.play(Write(calc_text))

        # Animate glucose thermometer dropping more
        g_temp_new = Text("269.06 K", font_size=24, color=YELLOW).next_to(g_therm, RIGHT)
        self.play(
            s_therm_liquid.animate.stretch_to_fit_height(2.0).align_to(s_therm_rect.get_bottom(), DOWN),
            g_therm_liquid.animate.stretch_to_fit_height(1.0).align_to(g_therm_rect.get_bottom(), DOWN),
            Transform(g_temp, g_temp_new),
            run_time=3
        )
        self.wait(5)


class Scene9(Scene):
    def construct(self):
        # Henry’s Law & Aquatic Life
        title = Text("Henry's Law & Aquatic Life", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Split screen lakes
        lake1 = Rectangle(width=5, height=3, color=BLUE, fill_opacity=0.3).move_to(LEFT*3 + DOWN*1)
        lake2 = Rectangle(width=5, height=3, color=BLUE, fill_opacity=0.3).move_to(RIGHT*3 + DOWN*1)

        l1_title = Text("Cold Water", font_size=30).next_to(lake1, UP)
        l2_title = Text("Warm Water", font_size=30).next_to(lake2, UP)

        self.play(FadeIn(lake1), FadeIn(lake2), Write(l1_title), Write(l2_title))

        # Thermometers
        t1 = Rectangle(width=0.2, height=2).move_to(LEFT*5 + DOWN*1)
        t1_liq = Rectangle(width=0.2, height=0.5, color=RED, fill_opacity=1).align_to(t1, DOWN)

        t2 = Rectangle(width=0.2, height=2).move_to(RIGHT*1 + DOWN*1)
        t2_liq = Rectangle(width=0.2, height=1.8, color=RED, fill_opacity=1).align_to(t2, DOWN)

        self.play(Create(t1), FadeIn(t1_liq), Create(t2), FadeIn(t2_liq))

        # Bubbles
        b1 = VGroup(*[Circle(radius=0.1, color=WHITE).move_to(LEFT*(1+np.random.rand()*3) + DOWN*(np.random.rand()*2)) for _ in range(15)])
        b2 = VGroup(*[Circle(radius=0.1, color=WHITE).move_to(RIGHT*(2+np.random.rand()*3) + DOWN*(np.random.rand()*2)) for _ in range(5)])

        self.play(FadeIn(b1), FadeIn(b2))

        # Escaping bubbles
        b_esc = VGroup(*[Circle(radius=0.1, color=WHITE).move_to(RIGHT*(2+np.random.rand()*3) + UP*0.5) for _ in range(10)])
        self.play(
            b_esc.animate.shift(UP*2),
            run_time=2
        )
        self.play(FadeOut(b_esc))

        # Equation and Graph
        eq = MathTex("C = kP", font_size=36).move_to(UP*2)

        ax = Axes(x_range=[0,1], y_range=[0,1], x_length=2, y_length=2).move_to(UP*2 + RIGHT*4)
        curve = ax.plot(lambda x: 1 - x, color=YELLOW)
        ax_l1 = Text("Temp", font_size=12).next_to(ax.x_axis, DOWN)
        ax_l2 = Text("Solubility", font_size=12).next_to(ax.y_axis, LEFT).rotate(PI/2)

        self.play(Write(eq), Create(ax), Create(curve), Write(ax_l1), Write(ax_l2))

        # Happy Fish
        fish = Ellipse(width=1, height=0.5, color=ORANGE, fill_opacity=1).move_to(LEFT*3 + DOWN*1.5)
        tail = Polygon(fish.get_left(), fish.get_left() + LEFT*0.3+UP*0.3, fish.get_left() + LEFT*0.3+DOWN*0.3, color=ORANGE, fill_opacity=1)
        eye = Dot(color=BLACK).move_to(fish.get_right() + LEFT*0.2 + UP*0.1)
        happy_fish = VGroup(fish, tail, eye)

        self.play(FadeIn(happy_fish))
        self.play(happy_fish.animate.shift(RIGHT*1), run_time=2)
        self.wait(5)


class Scene10(Scene):
    def construct(self):
        # Non-Ideal Solutions (Ethanol & Acetone)
        title = Text("Non-Ideal Solutions (Positive Deviation)", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Microscopic View
        box = Rectangle(width=5, height=4).move_to(LEFT*3 + DOWN*0.5)
        self.play(Create(box))

        ethanols = VGroup(*[Circle(radius=0.3, color=BLUE, fill_opacity=1).move_to(LEFT*(1+i*1.5) + DOWN*1) for i in range(3)])
        h_bonds = VGroup(
            Line(ethanols[0].get_right(), ethanols[1].get_left(), color=YELLOW, stroke_width=8),
            Line(ethanols[1].get_right(), ethanols[2].get_left(), color=YELLOW, stroke_width=8)
        )

        e_label = Text("Ethanol", font_size=20, color=BLUE).next_to(box, DOWN)
        self.play(FadeIn(ethanols), Create(h_bonds), Write(e_label))

        # Introduce Acetone
        acetones = VGroup(*[Circle(radius=0.25, color=RED, fill_opacity=1).move_to(LEFT*(1.75+i*1.5) + UP*1) for i in range(2)])
        a_label = Text("Acetone", font_size=20, color=RED).next_to(e_label, DOWN)

        self.play(FadeIn(acetones), Write(a_label))

        # Wedging and breaking bonds
        self.play(
            acetones[0].animate.move_to(h_bonds[0].get_center()),
            acetones[1].animate.move_to(h_bonds[1].get_center()),
            run_time=2
        )

        weak_bonds = VGroup(
            DashedLine(ethanols[0].get_right(), acetones[0].get_left(), color=WHITE, stroke_width=2),
            DashedLine(acetones[0].get_right(), ethanols[1].get_left(), color=WHITE, stroke_width=2),
            DashedLine(ethanols[1].get_right(), acetones[1].get_left(), color=WHITE, stroke_width=2),
            DashedLine(acetones[1].get_right(), ethanols[2].get_left(), color=WHITE, stroke_width=2)
        )

        self.play(FadeOut(h_bonds), FadeIn(weak_bonds))

        # Escaping to vapor
        self.play(
            ethanols.animate.shift(UP*2),
            acetones.animate.shift(UP*2),
            FadeOut(weak_bonds),
            run_time=2
        )

        # Raoult's Law Graph
        ax = Axes(x_range=[0,1], y_range=[0,1], x_length=4, y_length=4).move_to(RIGHT*3 + DOWN*0.5)
        ideal_curve = ax.plot(lambda x: x, color=WHITE)
        real_curve = ax.plot(lambda x: x + 0.3*np.sin(x*PI), color=RED)

        ax_l = Text("Positive Deviation", font_size=24, color=RED).next_to(ax, UP)

        self.play(Create(ax), Create(ideal_curve), Create(real_curve), Write(ax_l))
        self.wait(7)
