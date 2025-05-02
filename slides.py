from manim import *
from manim_slides import Slide


class Introduction(Slide):
    def construct(self):
        text_1_1, text_1_2 = VGroup(
            Text("Discrete Mathematics"),
            Text('"Welcome to hell..." -Tarun Naveen'),
        ).arrange(DOWN)

        square = Square(color=BLUE)
        dot = Dot(color=RED).shift(RIGHT + UP)

        self.next_slide()
        self.play(FadeIn(text_1_1))
        self.play(FadeIn(text_1_2))
        self.next_slide()

        self.wipe(text_1_1, square)
        self.play(FadeIn(dot))

        self.next_slide(loop=True)
        self.play(
            MoveAlongPath(dot, square, rate_func=linear), run_time=2
        )

class WithTeX(Slide):
    def construct(self):
        tex, text = VGroup(
            Tex(r"You can also use \TeX, e.g., $\cos\theta=1$"),
            Text("which does not render like plain text"),
        ).arrange(DOWN)

        self.play(FadeIn(tex))
        self.next_slide()

        self.play(FadeIn(text, shift=DOWN))


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
