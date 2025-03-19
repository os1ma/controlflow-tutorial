from dotenv import load_dotenv

load_dotenv()

import controlflow as cf


@cf.flow
def analyze_text(text: str):
    # Create a parent task to represent the entire analysis
    with cf.Task(
        "Analyze the given text",
        instructions="Include each subtask result in your result",
        result_type=dict,
        context={"text": text},
    ) as parent_task:
        # Child task 1: Identify key terms
        key_terms = cf.Task(
            "Identify up to 10 key terms in the text",
            result_type=list[str],
        )

        # Child task 2: Summarize (depends on key_terms)
        summary = cf.Task(
            "Summarize the text in one sentence",
            result_type=str,
            depends_on=[key_terms],
        )

    # Run the parent task, which will automatically run all child tasks
    result = parent_task.run()
    return result


# Execute the flow
text = """
    Agentic workflow orchestration refers to the coordination of autonomous
    agents within a structured workflow, allowing them to operate independently
    while achieving a common objective. Unlike traditional workflows that rigidly
    define tasks and dependencies, agentic workflows empower agents—typically
    AI-driven—to make decisions, prioritize tasks, and collaborate dynamically.
    Each agent in this system operates with a degree of autonomy, enabling it to
    adapt to changing conditions, handle uncertainties, and optimize its own
    actions within the broader workflow. This approach enhances flexibility and
    scalability, making it particularly effective for complex, multi-step
    processes where real-time adjustments and intelligent decision-making are
    crucial. By leveraging agents with defined roles and responsibilities, agentic
    workflows maintain structure while enabling innovation and responsiveness in
    task execution.
    """

result = analyze_text(text)
print(result)
