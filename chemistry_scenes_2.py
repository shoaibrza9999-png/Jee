from manim import *

class Scene4(Scene):
    def construct(self):
        # Mole Fraction of Ethylene Glycol
        title = Text("Mole Fraction of Ethylene Glycol", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Initial Beaker
        beaker = Rectangle(width=2, height=3, color=WHITE).move_to(LEFT*4 + DOWN*0.5)
        b_label = Text("100g\nSolution", font_size=24).move_to(beaker.get_center())

        self.play(Create(beaker), Write(b_label))
        self.wait(1)

        # Splitting
        self.play(beaker.animate.shift(RIGHT*2), b_label.animate.shift(RIGHT*2))

        block1 = Rectangle(width=2, height=0.6, color=GREEN, fill_opacity=0.8).move_to(RIGHT*2 + UP*0.5)
        lbl1 = Text("20g C_2H_6O_2", font_size=20).move_to(block1.get_center())

        block2 = Rectangle(width=2, height=2.4, color=BLUE, fill_opacity=0.8).move_to(RIGHT*2 + DOWN*1)
        lbl2 = Text("80g H_2O", font_size=20).move_to(block2.get_center())

        self.play(
            FadeOut(beaker), FadeOut(b_label),
            FadeIn(block1), FadeIn(lbl1),
            FadeIn(block2), FadeIn(lbl2)
        )
        self.wait(1)

        # Calculations
        eq1 = MathTex("n_{glycol} = \\frac{20\\text{ g}}{62\\text{ g/mol}} = 0.322\\text{ mol}", font_size=30).move_to(UP*0.5 + RIGHT*5)
        eq2 = MathTex("n_{water} = \\frac{80\\text{ g}}{18\\text{ g/mol}} = 4.444\\text{ mol}", font_size=30).move_to(DOWN*1 + RIGHT*5)

        self.play(
            block1.animate.shift(LEFT*2), lbl1.animate.shift(LEFT*2),
            block2.animate.shift(LEFT*2), lbl2.animate.shift(LEFT*2)
        )
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait(1)

        # Mole fraction formula
        formula = MathTex("\\chi = \\frac{n_A}{n_{total}}", font_size=36).move_to(DOWN*2.5 + LEFT*2)
        subst = MathTex("= \\frac{0.322}{0.322 + 4.444}", font_size=36).next_to(formula, RIGHT)
        ans = MathTex("= 0.068", font_size=36, color=YELLOW).next_to(subst, RIGHT)

        self.play(Write(formula))
        self.play(Write(subst))
        self.play(Write(ans))

        # Highlight final answer
        box = SurroundingRectangle(ans, color=YELLOW)
        self.play(Create(box))
        self.wait(7)


class Scene5(Scene):
    def construct(self):
        # Boiling Point Elevation
        title = Text("Boiling Point Elevation", font_size=40).to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"include_tip": True},
            x_length=6,
            y_length=5
        ).move_to(DOWN*0.5)

        labels = axes.get_axis_labels(
            Text("Temperature", font_size=24),
            Text("Vapor Pressure", font_size=24).rotate(PI/2)
        )

        self.play(Create(axes), Write(labels))

        # Pure Solvent Curve
        pure_curve = axes.plot(lambda x: 0.1 * x**2, color=WHITE, x_range=[0, 9])
        pure_label = Text("Pure Solvent", font_size=20).next_to(pure_curve, UP).shift(LEFT*1)

        self.play(Create(pure_curve), Write(pure_label))

        # 1 atm line
        atm_line = DashedLine(axes.c2p(0, 8), axes.c2p(10, 8), color=YELLOW)
        atm_label = Text("1 atm", font_size=20, color=YELLOW).next_to(atm_line, LEFT)

        self.play(Create(atm_line), Write(atm_label))

        # T_b^0
        x_intersect_1 = 8.94  # sqrt(80)
        p1 = axes.c2p(x_intersect_1, 8)
        p2 = axes.c2p(x_intersect_1, 0)
        line1 = DashedLine(p1, p2, color=WHITE)
        tb0_label = MathTex("T_b^0", font_size=24).next_to(p2, DOWN)

        self.play(Create(line1), Write(tb0_label))

        # Solution Curve
        sol_curve = axes.plot(lambda x: 0.08 * x**2, color=ORANGE, x_range=[0, 10])
        sol_label = Text("Solution", font_size=20, color=ORANGE).next_to(sol_curve, DOWN).shift(LEFT*1)

        self.play(Create(sol_curve), Write(sol_label))

        # T_b
        x_intersect_2 = 10.0  # sqrt(100)
        p3 = axes.c2p(x_intersect_2, 8)
        p4 = axes.c2p(x_intersect_2, 0)
        line2 = DashedLine(p3, p4, color=ORANGE)
        tb_label = MathTex("T_b", font_size=24, color=ORANGE).next_to(p4, DOWN)

        self.play(Create(line2), Write(tb_label))

        # Delta Tb arrow
        arrow = DoubleArrow(p2, p4, buff=0, color=RED).shift(DOWN*0.5)
        dtb_label = MathTex("\\Delta T_b", font_size=24, color=RED).next_to(arrow, DOWN)

        self.play(Create(arrow), Write(dtb_label))
        self.wait(5)


class Scene6(Scene):
    def construct(self):
        # Reverse Osmosis
        title = Text("Reverse Osmosis", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Tank
        tank = Rectangle(width=8, height=4, color=WHITE).move_to(DOWN*0.5)
        membrane = DashedLine(tank.get_top(), tank.get_bottom(), color=GRAY)
        m_label = Text("Semi-permeable Membrane", font_size=20).next_to(membrane, UP)

        self.play(Create(tank), Create(membrane), Write(m_label))

        # Saltwater vs Pure Water
        saltwater = Rectangle(width=3.95, height=3.95, color=BLUE, fill_opacity=0.3).move_to(tank.get_left() + RIGHT*2)
        purewater = Rectangle(width=3.95, height=3.95, color=BLUE, fill_opacity=0.1).move_to(tank.get_right() + LEFT*2)

        salt_label = Text("Saltwater", font_size=24).move_to(tank.get_left() + RIGHT*2 + UP*1.5)
        pure_label = Text("Pure Water", font_size=24).move_to(tank.get_right() + LEFT*2 + UP*1.5)

        self.play(FadeIn(saltwater), FadeIn(purewater), Write(salt_label), Write(pure_label))

        # Salt molecules
        salt_mols = VGroup(*[Circle(radius=0.1, color=WHITE, fill_opacity=1).move_to(tank.get_left() + RIGHT*(0.5 + 3*np.random.rand()) + DOWN*(1.5 - 3*np.random.rand())) for _ in range(20)])
        self.play(FadeIn(salt_mols))

        # Normal Osmosis Arrow
        osmosis_arrow = Arrow(RIGHT*1.5, LEFT*1.5, color=BLUE, buff=0).move_to(DOWN*0.5)
        osmosis_label = Text("Normal Osmosis", font_size=20, color=BLUE).next_to(osmosis_arrow, DOWN)

        self.play(Create(osmosis_arrow), Write(osmosis_label))
        self.wait(2)

        # Piston for Reverse Osmosis
        self.play(FadeOut(osmosis_arrow), FadeOut(osmosis_label))

        piston = Rectangle(width=3.95, height=0.5, color=GRAY, fill_opacity=1).move_to(tank.get_left() + RIGHT*2 + UP*2.25)
        p_label = MathTex("P > \\pi", font_size=30).next_to(piston, UP)

        self.play(Create(piston), Write(p_label))

        # Reverse Osmosis Arrow
        ro_arrow = Arrow(LEFT*1.5, RIGHT*1.5, color=RED, buff=0).move_to(DOWN*0.5)
        ro_label = Text("Reverse Osmosis", font_size=20, color=RED).next_to(ro_arrow, DOWN)

        # Animation: Piston moves down, water moves right, salt stays
        self.play(
            Create(ro_arrow), Write(ro_label),
            piston.animate.shift(DOWN*1.5),
            saltwater.animate.stretch_to_fit_height(2.45).align_to(tank.get_bottom(), DOWN),
            purewater.animate.stretch_to_fit_height(3.95).align_to(tank.get_bottom(), DOWN),
            run_time=3
        )

        # Application Text
        app_text = Text("Application: Desalination", font_size=30, color=YELLOW).to_edge(DOWN)
        self.play(Write(app_text))
        self.wait(5)
