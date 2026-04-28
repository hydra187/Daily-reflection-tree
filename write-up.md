# Daily Reflection Tree: Design Rationale

## 1. Why these specific questions?
The questions are designed to move the employee from **surface-level reactions to deep underlying structures**. 

- **Axis 1 (Locus: Victim vs. Victor):** I start with a simple check-in ("How would you describe today?") because asking someone to locate their agency requires first acknowledging their emotional state. If they had a tough day, I ask "When things got difficult, what was your first instinct?" Options like "Wait for someone to step in" capture external locus without sounding inherently "bad"—they represent a natural human response to being overwhelmed. The choices deliberately force a distinction between finding *what you can control* (Internal Locus) versus *feeling stuck* (External Locus).
- **Axis 2 (Orientation: Contribution vs. Entitlement):** This is often the hardest to self-diagnose. Entitlement is invisible to the person holding it. Therefore, I ask "Think about an interaction you had today. Were you giving or expecting?" The follow-up question ("What was the expectation there?") maps to Campbell's psychological entitlement model. Options like "I deserved better" reflect entitlement, whereas "I wanted to make things easier for them" reflects Organ's Organizational Citizenship Behavior (OCB).
- **Axis 3 (Radius: Self-Centrism vs. Altrocentrism):** The final axis broadens the scope based on Maslow's Self-Transcendence. By asking "When you think about today's biggest challenge, who comes to mind?", the tree measures the radius of concern. Narrowing focus is a natural trauma response to stress, so the options range from "Just me" to "The customer/end user." The follow-up gently nudges perspective-taking.

## 2. Branching Trade-offs
Designing a deterministic tree means accepting trade-offs in flexibility to guarantee predictability.
- **Trade-off: Categorical vs. Continuous.** Instead of treating agency as a slider from 0-10, the tree forces a categorical choice. This makes routing simple but risks missing nuance. To counter this, I implemented an "Axis Dominant" condition system. Even if they had one moment of external locus, the tree tracks the *dominant* signal across the axis to route them to the most relevant reflection.
- **Trade-off: Empathy vs. Objectivity.** The reflections must reframe without moralizing. A fully empathetic response might validate a victim mindset, while a purely objective one might sound like a manager reprimanding them. The reflections aim for the tone of a "wise colleague"—acknowledging the difficulty but challenging the perspective ("A tough day pulls attention outward... But somewhere in there, you made a call.").

## 3. Psychological Grounding
- **Julian Rotter (1954) - Locus of Control:** Formed the basis of Axis 1. The questions isolate whether the user views outcomes as contingent on their own behavior (internal) or on forces outside themselves (external).
- **Organ (1988) - Organizational Citizenship Behavior (OCB):** Axis 2 is built around discretionary effort. The questions don't just ask if someone worked hard; they ask *why* they worked hard (e.g., "It felt like the right thing to do" vs. "I wanted to be recognized").
- **Maslow (1969) / Batson (2011) - Self-Transcendence & Empathy:** Axis 3 is anchored in the idea that emotional pain at work is amplified by self-centeredness. The questions force cognitive perspective-taking, asking the user to zoom out and recognize their part in a larger system.

## 4. What I'd improve with more time
- **Deeper Sub-trees:** I would add 2-3 more questions per axis to capture a more granular psychological profile.
- **Cross-Axis Synthesis:** I would introduce bridging questions that dynamically reference *both* Axis 1 and Axis 2 before entering Axis 3 (e.g., "You handled the difficulty well (Internal Locus), but did you help others do the same? (Contribution)").
- **More Nuanced Summaries:** The summary combinations could be expanded from the basic 3 variations to 8 (2x2x2) unique end-state paragraphs.
