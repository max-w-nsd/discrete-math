from manim import *
from manim_slides import Slide
from math import comb


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

        # try out Group or VGroup instead of list?
        self.wipe([text_1_1, text_2_1, text_2_2])
        self.play(Write(text_3_1))
        self.play(FadeIn(apples_2, lag_ratio=0.1))
        self.play(Write(text_3_2))

        # ADDITIVE PRINCIPLE
        # self.next_slide()
        
        # text_4_1, text_4_2, text_4_3 = VGroup(
        #     Text("14 donuts"),
        #     Text("16 hotdogs"),
        #     Text("How many options are there?"),
        # ).arrange(DOWN)

        # self.wipe([text_3_1, text_3_2, apples_2])
        # self.play(Write(text_4_1), Write(text_4_2), Write(text_4_3))

        # self.next_slide()

        # text_5_1 = MathTex("14+16=30", font_size=72)
        # text_5_1.next_to(text_4_2, DOWN)

        # self.play(ReplacementTransform(text_4_3, text_5_1))

        # self.next_slide()

        # group_6 = VGroup(
        #     Text("Additive principle"),
        #     MathTex(r"A \text{or} B = A + B", font_size=72),
        # ).arrange(DOWN)

        # self.wipe([text_4_1, text_4_2, text_5_1], group_6)

        self.next_slide()

        lines = VGroup()
        for i in range(-6, 7, 3):
            lines.add(Line(i / 2 * RIGHT + 3 * UP, i / 2 * RIGHT + 3 * DOWN))
        for i in range(-6, 7, 3):
            lines.add(Line(i / 2 * DOWN + 3 * LEFT, i / 2 * DOWN + 3 * RIGHT))
        lines.shift(RIGHT * 3)
        
        squares = VGroup()
        numbers = VGroup()
        for i in range(4):
            for j in range(4):
                s = Square(1.5)
                if (i + j) % 2 == 1:
                    s.set_fill(GRAY_E, 1)
                s.align_to(lines[i], LEFT)
                s.align_to(lines[j + 5], UP)
                squares.add(s)
                n = MathTex(str(comb(i + j, j)), font_size=60)
                n.move_to(s)
                numbers.add(n)

        rook = SVGMobject("Chess_rlt45.svg", height=1)
        rook.move_to(squares[0])

        text_1 = Text("How many shortest\npaths are there to\neach square?", font_size=36)
        text_1.to_edge(LEFT)

        self.wipe([text_3_1, text_3_2, apples_2])
        self.play(Create(lines, lag_ratio=0.1))
        self.play(FadeIn(squares, lag_ratio=0.1))
        self.play(FadeIn(rook), Write(text_1), Write(numbers[10]))

        self.next_slide()

        n1 = numbers[10]
        numbers.remove(n1)
        numbers.remove(numbers[0])

        self.play(Write(numbers, lag_ratio=0.1))

        self.next_slide()

        text_2 = Text("Binomial Coefficient")
        text_2.to_edge(UP)
        text_3 = MathTex(r"\binom{n}{k} = \frac{n!}{k!(n-k)!}", font_size=72)

        self.wipe([lines, squares, numbers, n1, text_1, rook], text_2)
        self.play(Write(text_3))

        self.next_slide()

        text_4 = Text("With 6 pizza toppings, how many\ncombinations of two unique toppings\ncan be made?")
        text_4.to_edge(UP)

        self.wipe([text_2, text_3], text_4, direction=UP)

        self.next_slide()

        text_5 = MathTex(r"\binom{6}{2} = 15", font_size=72)

        self.play(Write(text_5))

        self.next_slide()

        lines = VGroup()
        for i in range(-4, 5):
            lines.add(Line(i * 0.75 * RIGHT + 3 * UP, i * 0.75 * RIGHT + 3 * DOWN))
        for i in range(-4, 5):
            lines.add(Line(i * 0.75 * DOWN + 3 * LEFT, i * 0.75 * DOWN + 3 * RIGHT))
        
        squares = VGroup()
        numbers = VGroup()
        for i in range(8):
            for j in range(8):
                s = Square(0.75)
                if (i + j) % 2 == 1:
                    s.set_fill(GRAY_E, 1)
                s.align_to(lines[i], LEFT)
                s.align_to(lines[j + 9], UP)
                squares.add(s)
                n = MathTex(str(comb(i + j, j)), font_size=36)
                n.move_to(s)
                numbers.add(n)
        
        rook = SVGMobject("Chess_rlt45.svg", height=0.5)
        rook.move_to(squares[0])

        self.wipe([text_4, text_5])
        self.play(Create(lines, lag_ratio=0.1))
        self.play(FadeIn(squares, lag_ratio=0.1))
        self.play(FadeIn(rook))

        self.next_slide()

        self.play(Write(numbers, lag_ratio=0.1))

        self.next_slide()

        text_6 = Text("How many ways can you distribute\n7 cookies to 4 kids?")
        text_6.to_edge(UP)

        self.wipe([lines, squares, numbers, rook], text_6)