from manim import *

class Scene1(Scene):
    def construct(self):
        # Molarity vs. Molality & Temperature Dependence
        title = Text("Molarity vs. Molality", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Split screen
        line = Line(UP*3, DOWN*3)
        self.play(Create(line))

        # Left: Molarity
        molarity_label = Text("Molarity (M)", font_size=30).move_to(LEFT*3 + UP*2)
        flask = VGroup(
            Line(LEFT*0.5, RIGHT*0.5).move_to(DOWN*1.5),
            Line(LEFT*0.5, LEFT*0.5 + UP*1).move_to(DOWN*1.5),
            Line(RIGHT*0.5, RIGHT*0.5 + UP*1).move_to(DOWN*1.5),
            Line(LEFT*0.5 + UP*1, LEFT*0.2 + UP*1.5).move_to(DOWN*1.5),
            Line(RIGHT*0.5 + UP*1, RIGHT*0.2 + UP*1.5).move_to(DOWN*1.5),
            Line(LEFT*0.2 + UP*1.5, LEFT*0.2 + UP*2.5).move_to(DOWN*1.5),
            Line(RIGHT*0.2 + UP*1.5, RIGHT*0.2 + UP*2.5).move_to(DOWN*1.5),
        ).move_to(LEFT*3 + DOWN*0.5)

        flask_liquid = Rectangle(width=1, height=1, color=BLUE, fill_opacity=0.5).move_to(LEFT*3 + DOWN*1)

        self.play(Write(molarity_label), Create(flask), FadeIn(flask_liquid))

        # Right: Molality
        molality_label = Text("Molality (m)", font_size=30).move_to(RIGHT*3 + UP*2)
        scale = Rectangle(width=2, height=0.5, color=GRAY, fill_opacity=1).move_to(RIGHT*3 + DOWN*1.5)
        beaker = VGroup(
            Line(LEFT*0.6, RIGHT*0.6).move_to(RIGHT*3 + DOWN*1.25),
            Line(LEFT*0.6, LEFT*0.6 + UP*1.5).move_to(RIGHT*3 + DOWN*1.25),
            Line(RIGHT*0.6, RIGHT*0.6 + UP*1.5).move_to(RIGHT*3 + DOWN*1.25)
        )
        beaker_liquid = Rectangle(width=1.2, height=1, color=BLUE, fill_opacity=0.5).move_to(RIGHT*3 + DOWN*0.75)
        beaker_label = Text("1 kg Solvent", font_size=20).move_to(RIGHT*3 + DOWN*0.75)

        self.play(Write(molality_label), Create(scale), Create(beaker), FadeIn(beaker_liquid), Write(beaker_label))

        # Animate blue dots (solute) dropping
        dots_left = VGroup(*[Dot(color=BLUE) for _ in range(5)]).arrange(RIGHT, buff=0.1).move_to(LEFT*3 + UP*1.5)
        dots_right = VGroup(*[Dot(color=BLUE) for _ in range(5)]).arrange(RIGHT, buff=0.1).move_to(RIGHT*3 + UP*1.5)

        self.play(FadeIn(dots_left), FadeIn(dots_right))
        self.play(
            dots_left.animate.move_to(LEFT*3 + DOWN*1),
            dots_right.animate.move_to(RIGHT*3 + DOWN*0.75),
            run_time=2
        )
        self.play(FadeOut(dots_left), FadeOut(dots_right))

        # Temperature slider
        slider_line = Line(LEFT*2, RIGHT*2).move_to(DOWN*3)
        slider_knob = Dot(color=RED).move_to(slider_line.get_left())
        temp_label = Text("Temperature", font_size=24, color=RED).next_to(slider_line, UP)

        self.play(Create(slider_line), FadeIn(slider_knob), Write(temp_label))
        self.wait(1)

        # Values
        m_val = DecimalNumber(1.0, num_decimal_places=2).move_to(LEFT*3 + UP*1)
        m_text = Text(" M", font_size=24).next_to(m_val, RIGHT)
        m_group = VGroup(m_val, m_text)

        mol_val = DecimalNumber(1.0, num_decimal_places=2).move_to(RIGHT*3 + UP*1)
        mol_text = Text(" m", font_size=24).next_to(mol_val, RIGHT)
        mol_group = VGroup(mol_val, mol_text)

        scale_val = Text("1.00 kg", font_size=20, color=BLACK).move_to(scale.get_center())

        self.play(Write(m_group), Write(mol_group), Write(scale_val))

        # Animate temperature increase
        self.play(
            slider_knob.animate.move_to(slider_line.get_right()),
            flask_liquid.animate.stretch_to_fit_height(1.5).move_to(LEFT*3 + DOWN*0.75),
            ChangeDecimalToValue(m_val, 0.85),
            run_time=4
        )
        self.wait(8)


class Scene2(Scene):
    def construct(self):
        # Raoult’s Law vs. Henry’s Law
        axes = Axes(
            x_range=[0, 1.2, 0.2],
            y_range=[0, 1.2, 0.2],
            axis_config={"include_tip": True},
            x_length=6,
            y_length=5
        ).move_to(DOWN*0.5)

        labels = axes.get_axis_labels(
            Text("Mole Fraction ($\chi$)", font_size=24),
            Text("Partial Pressure", font_size=24).rotate(PI/2)
        )

        self.play(Create(axes), Write(labels))

        # Raoult's Law line
        raoult_line = axes.plot(lambda x: 0.5 * x, color=WHITE, x_range=[0, 1])
        raoult_eq = MathTex("P_A = P_A^0 \chi_A", font_size=30).next_to(raoult_line, RIGHT).shift(UP*0.5)

        self.play(Create(raoult_line), Write(raoult_eq))

        # Henry's Law line
        henry_line = axes.plot(lambda x: 1.5 * x, color=BLUE, x_range=[0, 0.6])
        henry_eq = MathTex("P = K_H \chi", font_size=30, color=BLUE).next_to(henry_line.get_end(), UP)

        self.play(Create(henry_line), Write(henry_eq))
        self.wait(2)

        # Zoom in near origin
        zoom_circle = Circle(radius=1.5, color=YELLOW).move_to(axes.c2p(0.2, 0.2))
        self.play(Create(zoom_circle))

        zoom_text = Text("Lines conceptually merge at dilute concentrations", font_size=20, color=YELLOW).next_to(zoom_circle, RIGHT)
        self.play(Write(zoom_text))
        self.wait(2)

        # Text highlighting
        text_r = Text("Raoult's Law: Volatile Solvent", font_size=24).to_edge(UP).shift(LEFT*3)
        text_h = Text("Henry's Law: Dissolved Gas Solute", font_size=24, color=BLUE).to_edge(UP).shift(RIGHT*2)

        self.play(Write(text_r), Write(text_h))
        self.wait(9)


class Scene3(Scene):
    def construct(self):
        # Azeotropic Mixtures
        title = Text("Azeotropic Mixtures", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Dynamic temperature-composition phase diagram
        axes = Axes(
            x_range=[0, 1, 0.2],
            y_range=[70, 110, 10],
            axis_config={"include_tip": False},
            x_length=6,
            y_length=4
        ).move_to(DOWN*1)

        x_label = Text("Mole Fraction", font_size=20).next_to(axes.x_axis, DOWN)
        y_label = Text("Temperature (°C)", font_size=20).rotate(PI/2).next_to(axes.y_axis, LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Liquid and vapor curves (minimum boiling azeotrope example)
        # We will use simple quadratics to represent this
        liquid_curve = axes.plot(lambda x: 80 + 20*(x - 0.5)**2, color=BLUE, x_range=[0, 1])
        vapor_curve = axes.plot(lambda x: 80 + 80*(x - 0.5)**2, color=RED, x_range=[0, 1])

        self.play(Create(liquid_curve), Create(vapor_curve), run_time=2)

        # Azeotropic Point
        azeotrope_dot = Dot(color=YELLOW).move_to(axes.c2p(0.5, 80))
        dashed_line = DashedLine(axes.c2p(0.5, 80), axes.c2p(0.5, 70), color=YELLOW)
        azeotrope_label = Text("Azeotropic Point", font_size=20, color=YELLOW).next_to(dashed_line, DOWN)

        self.play(FadeIn(azeotrope_dot), Create(dashed_line), Write(azeotrope_label))
        self.wait(2)

        # Split screen for Min and Max
        self.play(
            FadeOut(axes), FadeOut(liquid_curve), FadeOut(vapor_curve),
            FadeOut(azeotrope_dot), FadeOut(dashed_line), FadeOut(azeotrope_label),
            FadeOut(x_label), FadeOut(y_label)
        )

        # Min Boiling
        ax_min = Axes(x_range=[0, 1], y_range=[0, 1], x_length=4, y_length=3).move_to(LEFT*3.5 + DOWN*1)
        curve_min = ax_min.plot(lambda x: 0.2 + 0.8*(x - 0.5)**2, color=BLUE)
        lbl_min = Text("Minimum Boiling", font_size=24).next_to(ax_min, UP)

        # Max Boiling
        ax_max = Axes(x_range=[0, 1], y_range=[0, 1], x_length=4, y_length=3).move_to(RIGHT*3.5 + DOWN*1)
        curve_max = ax_max.plot(lambda x: 0.8 - 0.6*(x - 0.5)**2, color=RED)
        lbl_max = Text("Maximum Boiling", font_size=24).next_to(ax_max, UP)

        self.play(Create(ax_min), Create(curve_min), Write(lbl_min),
                  Create(ax_max), Create(curve_max), Write(lbl_max))
        self.wait(2)

        # Flash molecular animation for max boiling
        flash_text = Text("Strong Hydrogen Bonds Forming!", font_size=24, color=YELLOW).move_to(RIGHT*3.5 + UP*1)
        h_bond = DashedLine(LEFT, RIGHT, color=YELLOW, stroke_width=8).move_to(RIGHT*3.5 + DOWN*1)

        self.play(Write(flash_text), Create(h_bond))
        self.play(Flash(h_bond, color=YELLOW, line_length=0.5))
        self.wait(1)
        self.play(FadeOut(flash_text), FadeOut(h_bond))
        self.wait(8)
