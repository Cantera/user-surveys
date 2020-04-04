def annotate_plot(ax, title, n_responses):
    ax.set_xlabel("Fraction of Responses")
    ax.set_title(title)
    for p in ax.patches:
        ax.annotate(
            str(int(p.get_width() * n_responses)),
            (p.get_x() + p.get_width(), p.get_y()),
            xytext=(3, 6),
            textcoords="offset points",
        )
