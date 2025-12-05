### 12/04/2025

7:08 PM

Recently I've been playing through all the dead space games and out of nowhere dead space 3 has this little scavenger robot that is so cute! OMG!

<img src="./devlog-images/robot.JPG"/>

Look at it, it has a little antenna and its head moves omg.

So yeah I just went ahead and ordered these N20 motors because I've seen these motors before other people using them but I've never used them myself, I mean I've used DC motors before with regards to RC planes but not programmatically via arduino.

So yeah this motor will determine the scale of this robot, each wheel will get one and it will be direct driven.

I had initially thought about wheels.

It will probably be slow but right now I'm more interested in making the entire system/shape of the body/painting PLA, that kind of thing, I think in the future you could do it right and swap it out with BLDC's.

I said arduino above but it will use an RPi, I have to see if the H-bridge thing can be commanded directly by the RPi (not powered by it).

And the head unit it'll be a single arducam, I have one I'm using for my IoT garden that I like, I'll get another one like that.

What I need to do is have it stream the video and pan/tilt its head so it doesn't need a massive view... although I will try and find a larger FOV camera just so you don't have to do so much stitching of separate images/frames

No the barrel thing around the lens will be 3D printed to match the size, will just use a V3 wide angle pi camera

The design is interesting because it's a mix of a legged and wheeled robot, it has a lot of joints and of course the little antenna/receiver dish thing has to spin
