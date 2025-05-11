from manim import *
from manim_slides import Slide


class Lesson1(Slide):
    def construct(self):
        text_1_1, text_1_2 = VGroup(
            Text("Discrete Mathematics", font_size=72),
            Text('"Welcome to hell..." -Tarun Naveen', color=GRAY),
        ).arrange(DOWN)

        self.play(FadeIn(text_1_1))
        self.play(FadeIn(text_1_2))
        self.next_slide()

        text_2_1 = Text("What is")
        text_2_2 = Text("?", font_size=72)

        text_2_1.next_to(text_1_2, UP)

        self.play(FadeOut(text_1_2, shift=DOWN), text_1_1.animate.shift(DOWN))
        text_2_2.next_to(text_1_1, RIGHT)
        self.play(Write(text_2_1))
        self.play(Write(text_2_2))

        self.next_slide()

        text_3_1 = Text("Lesson 1: Counting")
        text_3_2 = Text("How many apples are there?")

        a1 = ImageMobject("SnapdragonNEW.webp")
        a1.height = 1
        a2 = a1.copy()
        a3 = a1.copy()
        a4 = a1.copy()
        a5 = a1.copy()
        apples_1 = Group(a1, a2, a3, a4, a5).arrange(RIGHT)
        apples_2 = Group(apples_1, apples_1.copy()).arrange(DOWN)

        text_3_1.to_corner(UL)
        text_3_2.to_edge(DOWN)

        # TODO: try out Group or VGroup instead of list?
        self.wipe([text_1_1, text_2_1, text_2_2])
        self.play(Write(text_3_1))
        self.play(FadeIn(apples_2, lag_ratio=0.1))
        self.play(Write(text_3_2))


class WithTeX(Slide):
    def construct(self):
        tex = MathTex(r"\binom{n}{k} = \frac{n!}{k!(n-k)!}")

        self.play(FadeIn(tex))
        self.next_slide()


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
