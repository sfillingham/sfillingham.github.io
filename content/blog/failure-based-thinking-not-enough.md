Title: Why Failure-Based Thinking Is Not Enough for AI Safety
Date: 2026-03-27
Tags: STAMP, systems-safety, AI-governance
Summary: Most AI safety analysis asks "what happens when the model fails?" But some of the most important risks emerge when no component has failed at all. Systems-theoretic approaches offer a more complete lens.

*This post is cross-posted from [my Substack](https://yoursubstack.substack.com). Subscribe there to get new posts in your inbox.*

---

Most conversations about AI safety start with a simple question: *what happens when the model gets it wrong?*

This is a reasonable place to start. Models hallucinate. They produce harmful outputs. They fail to follow instructions. Understanding and mitigating these failure modes is important work, and I don't want to suggest otherwise.

But I want to argue that this framing — what I'll call **failure-based thinking** — is incomplete. And the gaps it leaves are precisely where some of the most consequential risks of frontier AI deployment live.

## The Failure-Based Paradigm

The dominant approach to AI safety focuses on scenarios where something goes wrong with the model itself. The model is misaligned with human intent. The model produces an incorrect or harmful output. The model fails to generalize. The model is jailbroken.

In each case, the analytical frame is: identify what can *fail*, estimate how likely and how bad the failure would be, and then mitigate it. This maps onto traditional risk assessment — hazard identification, probability estimation, consequence analysis.

This paradigm has roots in reliability engineering, where safety is achieved by making components more reliable and adding redundancy. If the component doesn't fail, the system is safe.

## Where It Falls Short

The problem is that in complex, tightly-coupled systems, **accidents can occur without any component failure at all**. This insight isn't new — it's the central thesis of systems safety engineering, developed over decades in aerospace, nuclear power, and medical devices.

Consider an agentic AI system that is deployed to manage a workflow. Every individual component — the model, the tool-use layer, the permissions system, the human oversight mechanism — is functioning exactly as designed. No component has "failed." But the *interactions between these components*, under conditions the designers didn't fully anticipate, produce an outcome that is unsafe.

This is not a model failure. It's a **control structure failure** — a breakdown in the constraints that are supposed to ensure safe behavior of the overall system.

## A Different Lens: STAMP

The Systems-Theoretic Accident Model and Processes (STAMP), developed by Nancy Leveson at MIT, provides a framework for thinking about safety that doesn't start with failure. Instead, it starts with **control**.

STAMP treats safety as a control problem. Systems are safe when adequate control is maintained over the processes that can lead to harm. Accidents occur when **safety constraints are violated** — and those violations can happen even when every individual component is working correctly.

The associated analysis method, STPA (System-Theoretic Process Analysis), works by modeling the control structure of a system and then systematically identifying how unsafe control actions can occur. It asks questions like:

- What control actions could lead to a hazard if provided incorrectly?
- What happens if a control action is provided at the wrong time, in the wrong sequence, or for too long?
- What if a necessary control action is *not* provided at all?

These questions are fundamentally different from "what if the model hallucinates?" — and they surface a different category of risk.

## What This Means for Frontier AI

As AI systems become more agentic — making decisions, taking actions, operating in multi-step workflows — the deployment environment becomes the primary source of systemic risk. The model is one component in a larger system that includes human operators, organizational processes, technical infrastructure, and regulatory constraints.

Failure-based analysis looks at the model. Systems-theoretic analysis looks at the *system* — and asks whether the control structure around that model is adequate to maintain safety under the conditions it will actually face.

I'll be writing more about how STPA can be concretely applied to frontier AI systems in upcoming posts. If this perspective resonates, [subscribe on Substack](https://yoursubstack.substack.com) to follow along.
