from manim import *
from manim_slides import Slide


class Introduction(Slide):
    def construct(self):
        text_1_1, text_1_2 = VGroup(
            Text("Discrete Mathematics", font_size=72),
            Text('"Welcome to hell..." -Tarun Naveen', color=GRAY),
        ).arrange(DOWN)

        square = Square(color=BLUE)
        dot = Dot(color=RED).shift(RIGHT + UP)

        self.play(FadeIn(text_1_1))
        self.play(FadeIn(text_1_2))
        self.next_slide(notes='testing out notes AAAAAAAAAAAAH')

        # TODO: try out Group or VGroup instead of list?
        # TODO: try out not including a group
        self.wipe([text_1_1, text_1_2], square)
        self.play(FadeIn(dot))

        self.next_slide(loop=True)
        self.play(
            MoveAlongPath(dot, square, rate_func=linear), run_time=2
        )

class WithTeX(Slide):
    def construct(self):
        tex, text = VGroup(
            Tex(r"{n\choose k}"),
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
