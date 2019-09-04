---
layout: default
title: Empathy Spot
---

# Welcome! 

If you've been invited to try out Empathy Spot, [click here to sign up or login](https://www.empathyspot.org/in/).

## Vision

To make it so that, at any time you choose, you can find someone to exchange empathy with via videochat. And to do this in a way that empowers NVC trainers and reinforces in-person communities.

## Current Status

The prototype for Empathy Spot is in an "alpha" phase of development and testing. You can see the [roadmap here](https://github.com/hugetim/empathyspot/projects/1) (currently under construction). [Click here to receive an email when Empathy Spot becomes open to the public.](http://eepurl.com/gAHrFT) 

## FAQ

### What is Empathy Spot?

A website focused exclusively on facilitating live empathy exchanges, or ["empathy buddy chats"](http://www.nycnvc.org/empathy_network/empathy-buddy-handbook/), including between people who have not previously met. 

### How is this different from other attempts to connect strangers online?

You are matched only with people authorized to participate by NVC trainers. Empathy Spot also aims to foster trust through:

* **Focus**: Nothing but empathy.
* **Privacy**: Your contact information and identity is kept private, and only communication directly related to empathy exchanges is allowed. 
* **Transparency**: [Open source code](https://github.com/hugetim/empathyspot) and financial transparency, funded by free-will offerings (so far, $24 for the domain name and lots of volunteer time).

### Is Empathy Spot for me?

* If you are a student of Compassionate Communication, a.k.a. [Nonviolent Communication (NVC)](http://www.nycnvc.org/our-work/), Empathy Spot is designed for you, particularly if you are connected with a certified NVC trainer. 
* If you are an NVC trainer, Empathy Spot is especially meant to be an asset for you and put you in control. 
* For others, Empathy Spot is not really intended for you, at least not at this point. Instead, consider connecting with a local [event](https://www.cnvc.org/trainings), [trainer](https://www.cnvc.org/trainers), or [community](https://www.cnvc.org/trainings/practice-groups).

### Why not let everyone use it?

Empathy Spot is not designed to teach people how to exchange empathy, and it also requires some form of gatekeeping to prevent unintended uses. So the idea, currently, is that NVC trainers will vouch for their students, authorizing them to match with other members to exchange empathy. 

### Is the website safe in terms of data security and privacy?

The Empathy Spot prototype is built using [Anvil](https://anvil.works/), an easy way to create web apps. It is considered [reputable in the Python development community](https://talkpython.fm/episodes/show/138/anvil-all-web-all-python). They seem to take [privacy](https://anvil.works/privacy) and [security](https://anvil.works/docs/security) seriously. They use [Amazon Web Services](https://www.sumologic.com/insight/aws/) under the hood.

The Anvil (python) code for Empathy Spot is [open source](https://github.com/hugetim/empathyspot), which doesn't provide much immediate reassurance but ultimately means that technically-inclined users will be able to inspect it themselves with regard to its privacy and security. In any case, the only information currently stored is your email address and activity on the site (basically, time stamps recording when you requested empathy and when you were successfully matched with someone for an empathy exchange). Any text chat logs are deleted once your empathy exchange is complete.

One inherent risk in participating via video chat is the possibility that the other person will secretly record you and share that recording with others. It may also be possible to use your image or voice to determine your identity. Voice-only and text-only options are available to mitigate this risk.

### What is Jitsi?

The video conferencing is provided via [Jitsi](https://github.com/jitsi/jitsi-meet), which is an open source project with an active community. It doesn't require account login, and it emphasizes privacy and security. It is owned by [8x8](https://www.8x8.com/about-us), which seems legit. (See [this interview with Jitsi's founder](https://www.8x8.com/blog/episode-5-meet-jitsi) for more on its origins.) The video conferencing is hosted separately from the Anvil webapp, so the Anvil app doesn't even see the video conference data.

### Who is making Empathy Spot?

Up until now, it has been the personal project of [Tim Huegerich](https://www.linkedin.com/in/tim-huegerich-26101a8/). But if anyone is interested in contributing, check out the [GitHub repository](https://github.com/hugetim/empathyspot) and [project roadmap](https://github.com/hugetim/empathyspot/projects/1) (under construction). Interested users can request features and influence design decisions in the [Empathy Spot discussion "Loomio"](https://www.loomio.org/g/CtW4A2KG/empathy-spot-discussion) or on [GitHub](https://github.com/hugetim/empathyspot/issues). (Work is ongoing to further develop these avenues. I (Tim) am fairly new at this and really welcome suggestions from more experienced developers&mdash;and others!)
