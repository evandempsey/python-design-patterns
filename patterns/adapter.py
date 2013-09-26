#!/usr/bin/env python


# Create abstract classes that define
# interfaces for independent classes we want to join.


class MediaPlayer(object):
    """
    Abstract class for media player.
    """

    def play(self, audioType, fileName):
        """
        Play an audio file.
        """
        raise NotImplementedError("play() method is not implemented.")


class AdvancedMediaPlayer(object):
    """
    Abstract class for advanced media player
    supporting more formats.
    """

    def playVlc(self, fileName):
        """
        Play a VLC file.
        """
        raise NotImplementedError("playVlc() method is not implemented.")

    def playMp4(self, fileName):
        """
        Play an MP4 file.
        """
        raise NotImplementedError("playMp4() method is not implemented.")


# Create concrete classes implementing methods in AdvancedMediaPlayer


class VlcPlayer(AdvancedMediaPlayer):
    """
    Player for VLC files.
    """

    def playVlc(self, fileName):
        """
        Play a VLC file.
        """
        print "playing VLC file: " + fileName


class Mp4Player(AdvancedMediaPlayer):
    """
    Player for MP4 files.
    """

    def playMp4(self, fileName):
        """
        Play an MP4 file.
        """
        print "playing MP4 file: " + fileName


# Create an adapter class that translates between MediaPlayer and AdvancedMediaPlayer


class MediaAdapter(MediaPlayer):
    """
    Adapter for MediaPlayer and AdvancedMediaPlayer.
    """

    def __init__(self, audioType):
        """
        Constructor builds player for correct type.
        """
        if audioType == "vlc":
            self.player = VlcPlayer()
        elif audioType == "mp4":
            self.player = Mp4Player()

    def play(self, audioType, fileName):
        """
        Play an audio file.
        """
        if audioType == "vlc":
            self.player.playVlc(fileName)
        elif audioType == "mp4":
            self.player.playMp4(fileName)


# Create a concrete class that extends MediaPlayer.


class AudioPlayer(MediaPlayer):
    """
    Player for different types of audio files.
    """

    def play(self, audioType, fileName):
        """
        Play the file.
        """

        # Class supports playing MP3 already.
        if audioType == "mp3":
            print "playing MP3 file: " + fileName

        # MediaAdapter supports other formats.
        elif audioType == "vlc" or audioType == "mp4":
            self.adapter = MediaAdapter(audioType)
            self.adapter.play(audioType, fileName)

        else:
            print "invalid media. " + audioType + " format not supported."


def main():
    """
    Test the adapter pattern implementation.
    """
    player = AudioPlayer()

    player.play("mp3", "When the Levee Breaks")
    player.play("vlc", "Trampled Underfoot")
    player.play("mp4", "Stairway to Heaven")
    player.play("m4a", "Communication Breakdown")


if __name__ == "__main__":
    main()