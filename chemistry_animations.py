from manim import *

class Question1(Scene):
    def construct(self):
        self.add_sound("audio.wav")
        # Define molarity and molality
        title = Text("Molarity vs Molality").to_edge(UP)
        self.play(Write(title))

        molarity_text = Text("Molarity (M): Volumetric Flask (1L)").scale(0.5).shift(LEFT*3 + UP*2)
        molality_text = Text("Molality (m): Weighing Balance (1kg)").scale(0.5).shift(RIGHT*3 + UP*2)

        # Flask representation
        flask = VGroup(
            Line(LEFT*0.5 + UP, LEFT*0.5 + DOWN*0.5),
            Line(RIGHT*0.5 + UP, RIGHT*0.5 + DOWN*0.5),
            ArcBetweenPoints(LEFT*0.5 + DOWN*0.5, RIGHT*0.5 + DOWN*0.5, angle=-PI)
        ).shift(LEFT*3 + DOWN)
        liquid = Rectangle(width=1, height=1, color=BLUE, fill_opacity=0.5).move_to(flask.get_bottom() + UP*0.5)

        # Balance representation
        balance = Line(LEFT, RIGHT).shift(RIGHT*3 + DOWN*1.5)
        mass = Rectangle(width=1, height=1, color=GREEN, fill_opacity=0.5).next_to(balance, UP, buff=0)

        self.play(Write(molarity_text), Write(molality_text))
        self.play(Create(flask), FadeIn(liquid), Create(balance), FadeIn(mass))

        # Temperature slider
        temp_text = Text("Temperature").scale(0.5).shift(DOWN*3)
        slider_line = Line(LEFT*2, RIGHT*2).next_to(temp_text, RIGHT)
        slider_dot = Dot().move_to(slider_line.get_start())
        self.play(Write(temp_text), Create(slider_line), FadeIn(slider_dot))

        # Animation of increasing temperature
        self.play(
            slider_dot.animate.move_to(slider_line.get_end()),
            liquid.animate.stretch_to_fit_height(1.5).move_to(flask.get_bottom() + UP*0.75),
            run_time=3
        )

        conclusion = Text("Molality is temperature independent!").scale(0.6).shift(DOWN*2)
        self.play(Write(conclusion))
        self.wait(2)

class Question2(Scene):
    def construct(self):
        self.add_sound("audio.wav")
        title = Text("Raoult's Law vs Henry's Law").to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[0, 1, 0.1],
            y_range=[0, 10, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False}
        ).shift(DOWN*0.5)

        labels = axes.get_axis_labels(x_label="Mole Fraction", y_label="Partial Pressure (P)")
        self.play(Create(axes), Write(labels))

        raoult_curve = axes.plot(lambda x: 8*x, color=WHITE)
        raoult_label = MathTex("P_A = P_A^0 \\chi_A", color=WHITE).next_to(raoult_curve, UP, buff=0.1).shift(LEFT)

        henry_curve = axes.plot(lambda x: 15*x, x_range=[0, 0.4], color=YELLOW)
        henry_label = MathTex("P = K_H \\chi", color=YELLOW).next_to(henry_curve, UP, buff=0.1)

        self.play(Create(raoult_curve), Write(raoult_label))
        self.play(Create(henry_curve), Write(henry_label))

        highlight_region = axes.get_area(henry_curve, x_range=[0, 0.2], color=YELLOW, opacity=0.3)
        dilute_text = Text("Dilute Region: Laws Converge", color=YELLOW).scale(0.4).next_to(highlight_region, RIGHT)
        self.play(FadeIn(highlight_region), Write(dilute_text))

        note = Text("Raoult's: Solvent | Henry's: Solute").scale(0.5).to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)

class Question3(Scene):
    def construct(self):
        self.add_sound("audio.wav")
        title = Text("Azeotropic Mixtures").to_edge(UP)
        self.play(Write(title))

        ax1 = Axes(x_range=[0, 1, 0.5], y_range=[0, 10, 5], x_length=4, y_length=3).shift(LEFT*3 + DOWN*0.5)
        ax2 = Axes(x_range=[0, 1, 0.5], y_range=[0, 10, 5], x_length=4, y_length=3).shift(RIGHT*3 + DOWN*0.5)

        title1 = Text("Minimum Boiling").scale(0.4).next_to(ax1, UP)
        title2 = Text("Maximum Boiling").scale(0.4).next_to(ax2, UP)

        self.play(Create(ax1), Create(ax2), Write(title1), Write(title2))

        # Minimum boiling curve
        liquid_curve_min = ax1.plot(lambda x: 8 - 4*x*(1-x), color=BLUE)
        vapor_curve_min = ax1.plot(lambda x: 8 - 6*x*(1-x), color=RED)
        azeo_point_min = Dot(ax1.coords_to_point(0.5, 7), color=YELLOW)

        # Maximum boiling curve
        liquid_curve_max = ax2.plot(lambda x: 2 + 4*x*(1-x), color=BLUE)
        vapor_curve_max = ax2.plot(lambda x: 2 + 6*x*(1-x), color=RED)
        azeo_point_max = Dot(ax2.coords_to_point(0.5, 3.5), color=YELLOW)

        self.play(Create(liquid_curve_min), Create(vapor_curve_min), FadeIn(azeo_point_min))
        self.play(Create(liquid_curve_max), Create(vapor_curve_max), FadeIn(azeo_point_max))

        note = Text("H-bonds affect deviation").scale(0.5).to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)

class Question4(Scene):
    def construct(self):
        self.add_sound("audio.wav")
        title = Text("Mole Fraction of Ethylene Glycol").to_edge(UP)
        self.play(Write(title))

        solution = Rectangle(width=4, height=1, color=WHITE).shift(UP*1.5)
        sol_text = Text("100g Solution").scale(0.5).move_to(solution)
        self.play(Create(solution), Write(sol_text))

        eg_rect = Rectangle(width=1.5, height=1, color=BLUE, fill_opacity=0.5).shift(UP*1.5 + LEFT*1.25)
        water_rect = Rectangle(width=2.5, height=1, color=TEAL, fill_opacity=0.5).shift(UP*1.5 + RIGHT*0.75)

        self.play(FadeIn(eg_rect), FadeIn(water_rect))

        eg_mass = Text("20g C2H6O2").scale(0.4).move_to(eg_rect)
        water_mass = Text("80g H2O").scale(0.4).move_to(water_rect)
        self.play(Transform(sol_text, VGroup(eg_mass, water_mass)))

        molar_mass_eg = MathTex("M_{EG} = 62 \\, g/mol").scale(0.6).shift(LEFT*2)
        molar_mass_w = MathTex("M_{H2O} = 18 \\, g/mol").scale(0.6).shift(RIGHT*2)
        self.play(Write(molar_mass_eg), Write(molar_mass_w))

        moles_eg = MathTex("n_{EG} = \\frac{20}{62} = 0.322 \\, mol").scale(0.6).next_to(molar_mass_eg, DOWN)
        moles_w = MathTex("n_{H2O} = \\frac{80}{18} = 4.444 \\, mol").scale(0.6).next_to(molar_mass_w, DOWN)
        self.play(Write(moles_eg), Write(moles_w))

        fraction = MathTex("\\chi_{EG} = \\frac{n_{EG}}{n_{EG} + n_{H2O}}").scale(0.7).shift(DOWN*1.5)
        result = MathTex("\\chi_{EG} = \\frac{0.322}{0.322 + 4.444} = 0.068").scale(0.7).next_to(fraction, DOWN)
        self.play(Write(fraction))
        self.play(Write(result))
        self.wait(2)

class Question5(Scene):
    def construct(self):
        self.add_sound("audio.wav")
        title = Text("Elevation of Boiling Point").to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 2, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False}
        ).shift(DOWN*0.5)

        labels = axes.get_axis_labels(x_label="Temperature (T)", y_label="Vapor Pressure (VP)")
        self.play(Create(axes), Write(labels))

        solvent_curve = axes.plot(lambda x: 0.05 * x**2, x_range=[0, 6], color=BLUE)
        solution_curve = axes.plot(lambda x: 0.05 * x**2 - 0.2, x_range=[2.5, 6.5], color=RED)

        solv_label = Text("Pure Solvent", color=BLUE).scale(0.4).next_to(solvent_curve, UP).shift(LEFT*2)
        soln_label = Text("Solution", color=RED).scale(0.4).next_to(solution_curve, DOWN)

        self.play(Create(solvent_curve), Write(solv_label))
        self.play(Create(solution_curve), Write(soln_label))

        atm_line = axes.get_horizontal_line(axes.coords_to_point(7, 1), color=WHITE, line_func=DashedLine)
        atm_label = Text("1 atm", color=WHITE).scale(0.4).next_to(atm_line, LEFT)
        self.play(Create(atm_line), Write(atm_label))

        # Intersection points
        # 0.05 * x^2 = 1 => x^2 = 20 => x = ~4.47
        # 0.05 * x^2 - 0.2 = 1 => 0.05 * x^2 = 1.2 => x^2 = 24 => x = ~4.90
        p1 = axes.coords_to_point(4.47, 1)
        p2 = axes.coords_to_point(4.90, 1)

        d1 = DashedLine(p1, axes.coords_to_point(4.47, 0), color=BLUE)
        d2 = DashedLine(p2, axes.coords_to_point(4.90, 0), color=RED)
        self.play(Create(d1), Create(d2))

        delta_t = MathTex("\\Delta T_b").scale(0.6).next_to(axes.coords_to_point(4.685, 0), DOWN)
        self.play(Write(delta_t))
        self.wait(2)

class Question6(Scene):
    def construct(self):
        self.add_sound("audio.wav")
        title = Text("Reverse Osmosis").to_edge(UP)
        self.play(Write(title))

        container = Rectangle(width=6, height=3, color=WHITE).shift(DOWN*0.5)
        membrane = DashedLine(container.get_top(), container.get_bottom(), color=YELLOW)
        self.play(Create(container), Create(membrane))

        salt_label = Text("Saltwater", color=BLUE).scale(0.5).move_to(container).shift(LEFT*1.5 + UP*1)
        pure_label = Text("Pure Water", color=TEAL).scale(0.5).move_to(container).shift(RIGHT*1.5 + UP*1)
        self.play(Write(salt_label), Write(pure_label))

        salt_particles = VGroup(*[Circle(radius=0.1, color=GRAY, fill_opacity=1).move_to(container.get_center() + LEFT*(np.random.random()*2.5 + 0.2) + DOWN*(np.random.random()*2.5 - 1.25)) for _ in range(10)])
        water_particles = VGroup(*[Circle(radius=0.05, color=BLUE, fill_opacity=1).move_to(container.get_center() + RIGHT*(np.random.random()*2.5 + 0.2) + DOWN*(np.random.random()*2.5 - 1.25)) for _ in range(20)])
        water_left = VGroup(*[Circle(radius=0.05, color=BLUE, fill_opacity=1).move_to(container.get_center() + LEFT*(np.random.random()*2.5 + 0.2) + DOWN*(np.random.random()*2.5 - 1.25)) for _ in range(15)])

        self.play(FadeIn(salt_particles), FadeIn(water_particles), FadeIn(water_left))

        osmosis_arrow = Arrow(RIGHT*1.5, LEFT*1.5, color=TEAL).shift(DOWN*0.5)
        osm_text = Text("Osmosis").scale(0.4).next_to(osmosis_arrow, UP)
        self.play(Create(osmosis_arrow), Write(osm_text))
        self.wait(1)

        self.play(FadeOut(osmosis_arrow), FadeOut(osm_text))

        pressure_arrow = Arrow(LEFT*4, LEFT*2, color=RED, stroke_width=8).shift(UP*0.5)
        p_text = MathTex("P > \\pi", color=RED).next_to(pressure_arrow, UP)
        self.play(Create(pressure_arrow), Write(p_text))

        ro_arrow = Arrow(LEFT*1.5, RIGHT*1.5, color=BLUE).shift(DOWN*0.5)
        self.play(Create(ro_arrow))

        self.play(
            water_left.animate.shift(RIGHT*3),
            run_time=2
        )

        app_text = Text("Application: Desalination").scale(0.5).to_edge(DOWN)
        self.play(Write(app_text))
        self.wait(2)

class Question7(Scene):
    def construct(self):
        self.add_sound("audio.wav")
        title = Text("van't Hoff Factor (i)").to_edge(UP)
        self.play(Write(title))

        lattice = VGroup(
            Circle(radius=0.2, color=GREEN, fill_opacity=1).shift(LEFT*0.2 + UP*0.2),
            Circle(radius=0.2, color=YELLOW, fill_opacity=1).shift(RIGHT*0.2 + UP*0.2),
            Circle(radius=0.2, color=YELLOW, fill_opacity=1).shift(LEFT*0.2 + DOWN*0.2),
            Circle(radius=0.2, color=GREEN, fill_opacity=1).shift(RIGHT*0.2 + DOWN*0.2)
        ).shift(UP*1)

        nacl_text = Text("NaCl Lattice").scale(0.5).next_to(lattice, UP)
        self.play(FadeIn(lattice), Write(nacl_text))

        water = Rectangle(width=8, height=3, color=BLUE, fill_opacity=0.3).shift(DOWN*1.5)
        self.play(Create(water))
        self.play(lattice.animate.move_to(water.get_center()))

        na1 = Circle(radius=0.2, color=GREEN, fill_opacity=1).move_to(water.get_center() + LEFT*1 + UP*0.5)
        cl1 = Circle(radius=0.2, color=YELLOW, fill_opacity=1).move_to(water.get_center() + RIGHT*1 + UP*0.5)
        na2 = Circle(radius=0.2, color=GREEN, fill_opacity=1).move_to(water.get_center() + RIGHT*1.5 + DOWN*0.5)
        cl2 = Circle(radius=0.2, color=YELLOW, fill_opacity=1).move_to(water.get_center() + LEFT*1.5 + DOWN*0.5)

        self.play(Transform(lattice, VGroup(na1, cl1, na2, cl2)))

        count_left = Text("1 formula unit added").scale(0.5).shift(LEFT*3)
        count_right = Text("2 ions produced").scale(0.5).shift(RIGHT*3)
        self.play(Write(count_left), Write(count_right))

        formula = MathTex("i = \\frac{\\text{Observed Particles}}{\\text{Calculated Particles}}").shift(UP*2)
        self.play(Transform(nacl_text, formula))

        result = MathTex("i = 2", color=YELLOW).scale(1.5).move_to(formula.get_center() + DOWN*1)
        box = SurroundingRectangle(result, color=YELLOW)
        self.play(Write(result), Create(box))
        self.wait(2)

class Question8(Scene):
    def construct(self):
        self.add_sound("audio.wav")
        title = Text("Depression of Freezing Point").to_edge(UP)
        self.play(Write(title))

        sugar_rect = Rectangle(width=3, height=2, color=WHITE).shift(LEFT*3 + UP*0.5)
        gluc_rect = Rectangle(width=3, height=2, color=WHITE).shift(RIGHT*3 + UP*0.5)

        sugar_text = Text("5% Cane Sugar").scale(0.4).next_to(sugar_rect, UP)
        gluc_text = Text("5% Glucose").scale(0.4).next_to(gluc_rect, UP)
        self.play(Create(sugar_rect), Create(gluc_rect), Write(sugar_text), Write(gluc_text))

        sugar_mol = Circle(radius=0.4, color=ORANGE, fill_opacity=0.8).move_to(sugar_rect)
        s_molar = MathTex("M = 342").scale(0.4).next_to(sugar_mol, DOWN)

        gluc_mols = VGroup(
            Circle(radius=0.2, color=RED, fill_opacity=0.8).move_to(gluc_rect.get_center() + LEFT*0.5),
            Circle(radius=0.2, color=RED, fill_opacity=0.8).move_to(gluc_rect.get_center() + RIGHT*0.5)
        )
        g_molar = MathTex("M = 180").scale(0.4).next_to(gluc_mols, DOWN)

        self.play(FadeIn(sugar_mol), Write(s_molar), FadeIn(gluc_mols), Write(g_molar))

        # Temperature scales
        scale1 = Line(LEFT*3 + DOWN*1, LEFT*3 + DOWN*3)
        scale2 = Line(RIGHT*3 + DOWN*1, RIGHT*3 + DOWN*3)
        self.play(Create(scale1), Create(scale2))

        t0_1 = DashedLine(LEFT*3.5 + DOWN*1.5, LEFT*2.5 + DOWN*1.5, color=BLUE)
        t0_2 = DashedLine(RIGHT*3.5 + DOWN*1.5, RIGHT*2.5 + DOWN*1.5, color=BLUE)
        t0_text = Text("273.15 K", color=BLUE).scale(0.4).move_to(DOWN*1.5)
        self.play(Create(t0_1), Create(t0_2), Write(t0_text))

        tf_s = DashedLine(LEFT*3.5 + DOWN*2, LEFT*2.5 + DOWN*2, color=ORANGE)
        tf_s_text = Text("271 K", color=ORANGE).scale(0.4).next_to(tf_s, LEFT)
        self.play(Create(tf_s), Write(tf_s_text))

        tf_g = DashedLine(RIGHT*3.5 + DOWN*2.8, RIGHT*2.5 + DOWN*2.8, color=RED)
        tf_g_text = Text("Lower Tf", color=RED).scale(0.4).next_to(tf_g, RIGHT)

        formula = MathTex("\\Delta T_f = K_f \\cdot m").scale(0.6).move_to(DOWN*2.5)
        self.play(Write(formula))
        self.play(Create(tf_g), Write(tf_g_text))

        note = Text("Lower Molar Mass -> More particles -> Greater depression").scale(0.4).to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)

class Question9(Scene):
    def construct(self):
        self.add_sound("audio.wav")
        title = Text("Henry's Law & Aquatic Life").to_edge(UP)
        self.play(Write(title))

        cold_tank = Rectangle(width=3, height=4, color=BLUE, fill_opacity=0.3).shift(LEFT*3)
        warm_tank = Rectangle(width=3, height=4, color=RED, fill_opacity=0.3).shift(RIGHT*3)

        cold_text = Text("Cold Water", color=BLUE).scale(0.5).next_to(cold_tank, UP)
        warm_text = Text("Warm Water", color=RED).scale(0.5).next_to(warm_tank, UP)
        self.play(Create(cold_tank), Create(warm_tank), Write(cold_text), Write(warm_text))

        # Dissolved Oxygen
        cold_o2 = VGroup(*[Circle(radius=0.1, color=GREEN, fill_opacity=1).move_to(cold_tank.get_center() + LEFT*(np.random.random()*1.2) + RIGHT*(np.random.random()*1.2) + UP*(np.random.random()*1.8) + DOWN*(np.random.random()*1.8)) for _ in range(15)])
        warm_o2 = VGroup(*[Circle(radius=0.1, color=GREEN, fill_opacity=1).move_to(warm_tank.get_center() + LEFT*(np.random.random()*1.2) + RIGHT*(np.random.random()*1.2) + UP*(np.random.random()*1.8) + DOWN*(np.random.random()*1.8)) for _ in range(5)])

        self.play(FadeIn(cold_o2), FadeIn(warm_o2))

        # Escaping oxygen in warm water
        escaping_o2 = VGroup(*[Circle(radius=0.1, color=GREEN, fill_opacity=1).move_to(warm_tank.get_top() + DOWN*0.2 + LEFT*(np.random.random()*1) + RIGHT*(np.random.random()*1)) for _ in range(5)])
        self.play(FadeIn(escaping_o2))
        self.play(escaping_o2.animate.shift(UP*1.5).set_opacity(0), run_time=2)

        formula = MathTex("C = k P").scale(0.8).move_to(UP*2)
        rel = Text("Solubility drops as Temp rises").scale(0.5).next_to(formula, DOWN)
        self.play(Write(formula), Write(rel))

        fish = Text("🐟").scale(2).move_to(cold_tank.get_center())
        happy = Text("Happy!").scale(0.5).next_to(fish, DOWN)
        self.play(FadeIn(fish), Write(happy))
        self.wait(2)

class Question10(Scene):
    def construct(self):
        self.add_sound("audio.wav")
        title = Text("Non-Ideal Solutions (Positive Deviation)").to_edge(UP)
        self.play(Write(title))

        # Molecules
        eth1 = Circle(radius=0.3, color=BLUE, fill_opacity=0.8).shift(LEFT*2 + UP*1)
        eth2 = Circle(radius=0.3, color=BLUE, fill_opacity=0.8).shift(RIGHT*2 + UP*1)
        hbond = DashedLine(eth1, eth2, color=YELLOW, stroke_width=4)
        hbond_text = Text("Strong H-Bond").scale(0.4).next_to(hbond, UP)

        self.play(FadeIn(eth1), FadeIn(eth2), Create(hbond), Write(hbond_text))

        ace = Circle(radius=0.3, color=RED, fill_opacity=0.8).shift(UP*3)
        self.play(FadeIn(ace))
        self.play(ace.animate.move_to(UP*1))

        # Bond breaks
        weak_bond1 = DashedLine(eth1, ace, color=GRAY)
        weak_bond2 = DashedLine(eth2, ace, color=GRAY)
        weak_text = Text("Weaker interactions").scale(0.4).next_to(ace, DOWN)

        self.play(FadeOut(hbond), FadeOut(hbond_text), Create(weak_bond1), Create(weak_bond2), Write(weak_text))

        self.play(
            eth1.animate.shift(UP*2 + LEFT),
            eth2.animate.shift(UP*2 + RIGHT),
            ace.animate.shift(UP*2),
            run_time=2
        )

        # Graph
        axes = Axes(x_range=[0, 1, 0.5], y_range=[0, 10, 5], x_length=4, y_length=3).shift(DOWN*1.5)
        self.play(Create(axes))

        ideal_curve = axes.plot(lambda x: 2 + 6*x, color=WHITE, stroke_width=2).set_opacity(0.5)
        dev_curve = axes.plot(lambda x: 2 + 6*x + 4*x*(1-x), color=GREEN)

        self.play(Create(ideal_curve))
        self.play(Create(dev_curve))

        dev_text = Text("Positive Deviation", color=GREEN).scale(0.4).next_to(dev_curve, UP)
        self.play(Write(dev_text))
        self.wait(2)
