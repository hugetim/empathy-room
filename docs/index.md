---
layout: default
title: Empathy Spot
---

# Welcome! 

If you've been invited to try out Empathy Spot, [click here to sign up or login](https://www.empathyspot.org/in/).

## Current Status

The prototype for Empathy Spot is in an "alpha" phase of development and testing. You can see the [roadmap here](https://github.com/hugetim/empathyspot/projects/1) (currently under construction). [Click here to receive an email when Empathy Spot becomes open to the public.](http://eepurl.com/gAHrFT) 

## FAQ

### Is the website safe in terms of data security and privacy?

The Empathy Spot prototype is built using [Anvil](https://anvil.works/), an easy way to create web apps. It is considered [reputable in the Python development community](https://talkpython.fm/episodes/show/138/anvil-all-web-all-python). They seem to take [privacy](https://anvil.works/privacy) and [security](https://anvil.works/docs/security) seriously. They use [Amazon Web Services](https://www.sumologic.com/insight/aws/) under the hood.

The Anvil (python) code for Empathy Spot is [open source](https://github.com/hugetim/empathyspot), which doesn't provide much immediate reassurance but ultimately means that technically-inclined users will be able to inspect it themselves with regard to its privacy and security. In any case, the only information currently stored is your email address and activity on the site (basically, time stamps recording when you requested empathy and when you were successfully matched with someone for an empathy exchange). Any text chat logs are deleted once your empathy exchange is complete.

One inherent risk in participating via video chat is the possibility that the other person will secretly record you and share that recording with others. It may also be possible to use your image or voice to determine your identity. Voice-only and text-only options are available to mitigate this risk.

### What is Jitsi?

The video conferencing is provided via [Jitsi](https://github.com/jitsi/jitsi-meet), which is an open source project with an active community. It doesn't require account login, and it emphasizes privacy and security. It is owned by [8x8](https://www.8x8.com/about-us), which seems legit. (See [this interview with Jitsi's founder](https://www.8x8.com/blog/episode-5-meet-jitsi) for more on its origins.) The video conferencing is hosted separately from the Anvil webapp, so the Anvil app doesn't even see the video conference data.

### Who is making Empathy Spot?

Up until now, it has been the personal project of [Tim Huegerich](https://www.linkedin.com/in/tim-huegerich-26101a8/). But if anyone is interested in contributing, check out the [GitHub repository](https://github.com/hugetim/empathyspot) and [project roadmap](https://github.com/hugetim/empathyspot/projects/1) (under construction).
