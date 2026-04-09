# =============================================================================
#  INSTALL ALL REQUIRED LIBRARIES + FFMPEG SETUP
# =============================================================================

import subprocess, sys, os

def pip_install(package):
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", package, "-q"],
        capture_output=True, text=True
    )
    print(f"  {'✅' if result.returncode == 0 else '❌'} {package}")

print("Installing libraries...")
for lib in ["ytmusicapi", "yt-dlp", "librosa", "scipy",
            "scikit-learn", "numpy", "pandas", "matplotlib", "imageio[ffmpeg]"]:
    pip_install(lib)

print("\n✅ All libraries installed!")

# =============================================================================
#  FFMPEG SETUP — uses full path, no admin rights needed
# =============================================================================

import imageio_ffmpeg

# Get the full path to the ffmpeg binary bundled with imageio
FFMPEG_PATH = imageio_ffmpeg.get_ffmpeg_exe()
print(f"\n✅ ffmpeg found at: {FFMPEG_PATH}")

# Verify it works by calling it directly with its full path
result = subprocess.run(
    [FFMPEG_PATH, "-version"],
    capture_output=True, text=True
)

if result.returncode == 0:
    print(f"✅ ffmpeg works: {result.stdout.split(chr(10))[0]}")
else:
    print(f"❌ ffmpeg error: {result.stderr[:100]}")

print("\n✅ Setup complete! All cells below will use FFMPEG_PATH directly.")

import os
import json
import time
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import RobustScaler
from sklearn.neighbors      import NearestNeighbors
from sklearn.decomposition  import PCA
from scipy                  import signal as scipy_signal
from scipy.io               import wavfile

warnings.filterwarnings("ignore")

# YouTube Music API
try:
    from ytmusicapi import YTMusic
    print("✅ ytmusicapi imported")
except ImportError:
    print("❌ ytmusicapi not found. Run: pip install ytmusicapi")

# librosa for audio feature extraction
try:
    import librosa
    print("✅ librosa imported")
except ImportError:
    print("❌ librosa not found. Run: pip install librosa")

# yt-dlp for downloading audio
try:
    import yt_dlp
    print("✅ yt-dlp imported")
except ImportError:
    print("❌ yt-dlp not found. Run: pip install yt-dlp")

print("\n✅ All imports done!")

# Create output folders
os.makedirs("bollywood_audio",  exist_ok=True)
os.makedirs("mix_outputs",      exist_ok=True)
print("✅ Output folders created")

import os
import json
import time
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import RobustScaler
from sklearn.neighbors      import NearestNeighbors
from sklearn.decomposition  import PCA
from scipy                  import signal as scipy_signal
from scipy.io               import wavfile

warnings.filterwarnings("ignore")

# YouTube Music API
try:
    from ytmusicapi import YTMusic
    print("✅ ytmusicapi imported")
except ImportError:
    print("❌ ytmusicapi not found. Run: pip install ytmusicapi")

# librosa for audio feature extraction
try:
    import librosa
    print("✅ librosa imported")
except ImportError:
    print("❌ librosa not found. Run: pip install librosa")

# yt-dlp for downloading audio
try:
    import yt_dlp
    print("✅ yt-dlp imported")
except ImportError:
    print("❌ yt-dlp not found. Run: pip install yt-dlp")

print("\n✅ All imports done!")

# Create output folders
os.makedirs("bollywood_audio",  exist_ok=True)
os.makedirs("mix_outputs",      exist_ok=True)
print("✅ Output folders created")

CLIP_SECS = 120
def fetch_songs_ytmusic(artists, songs_per_artist=7):
    """Fetches songs using multiple search strategies per artist."""
    print("=" * 65)
    print("  FETCHING BOLLYWOOD SONGS FROM YOUTUBE MUSIC")
    print("=" * 65)
    print(f"  Target: {songs_per_artist} songs per artist, {len(artists)} artists\n")

    ytm       = YTMusic()
    all_songs = []
    seen_ids  = set()
    failed    = []

    def add_song(song, artist_name):
        vid = song.get("videoId")
        if not vid or vid in seen_ids:
            return False
        seen_ids.add(vid)
        dur = 0
        if song.get("duration_seconds"):
            dur = int(song["duration_seconds"])
        elif song.get("duration"):
            try:
                parts = str(song["duration"]).split(":")
                dur   = int(parts[0])*60 + int(parts[1]) if len(parts)==2 else 0
            except: dur = 0
        if dur == 0: dur = CLIP_SECS
        all_songs.append({
            "video_id":    vid,
            "title":       song.get("title","Unknown"),
            "artist":      artist_name,
            "album":       song.get("album",{}).get("name","") if isinstance(song.get("album"),dict) else "",
            "duration_sec":dur,
            "youtube_url": f"https://www.youtube.com/watch?v={vid}",
        })
        return True

    for i, artist_name in enumerate(artists):
        print(f"  [{i+1:02d}/{len(artists)}] {artist_name}...", end=" ", flush=True)
        count_before = len(all_songs)
        try:
            # Strategy 1: artist page
            results = ytm.search(artist_name, filter="artists", limit=1)
            if results:
                aid = results[0].get("browseId")
                if aid:
                    for song in ytm.get_artist(aid).get("songs",{}).get("results",[]):
                        add_song(song, artist_name)

            # Strategy 2-6: search queries
            queries = [
                f"{artist_name}",
                f"{artist_name} hit songs",
                f"{artist_name} best songs",
                f"{artist_name} new songs",
                f"{artist_name} bollywood",
                f"{artist_name} popular",
            ]
            for query in queries:
                if len(all_songs) - count_before >= songs_per_artist: break
                try:
                    for song in ytm.search(query, filter="songs", limit=10):
                        if len(all_songs) - count_before >= songs_per_artist: break
                        arts = [a.get("name","").lower() for a in (song.get("artists") or [])]
                        if any(artist_name.lower().split()[0] in a for a in arts) or not arts:
                            add_song(song, artist_name)
                    time.sleep(0.1)
                except: continue

            print(f"✅ {len(all_songs)-count_before} songs")
            time.sleep(0.3)
        except Exception as e:
            print(f"❌ {str(e)[:50]}")
            failed.append(artist_name)
            time.sleep(0.5)

    df = pd.DataFrame(all_songs).drop_duplicates(subset=["video_id"]).reset_index(drop=True)
    print(f"\n✅ Total unique songs: {len(df)}  across {df['artist'].nunique()} artists")
    if failed: print(f"⚠  Failed: {', '.join(failed[:8])}")
    df.to_csv("bollywood_ytmusic_songs.csv", index=False)
    return df

songs_df = fetch_songs_ytmusic(BOLLYWOOD_ARTISTS, songs_per_artist=7)
print(songs_df[["title","artist","duration_sec"]].head(10).to_string(index=False))

# =============================================================================
#  DOWNLOAD AUDIO CLIPS AND EXTRACT FEATURES USING LIBROSA
#
#  For each song we:
#  1. Download a 30-second audio clip using yt-dlp
#  2. Extract audio features using librosa:
#     - tempo (BPM)
#     - energy (RMS)
#     - spectral centroid (brightness)
#     - spectral rolloff
#     - zero crossing rate (noisiness)
#     - MFCCs (timbre — 13 coefficients)
#     - chroma features (harmony — 12 notes)
# =============================================================================

AUDIO_DIR  = "bollywood_audio"
SAMPLE_RATE = 44100
CLIP_SECS   = 120    # seconds to download per song

def download_audio_clip(video_id, title, artist, output_dir=AUDIO_DIR):
    """
    Downloads a 30-second audio clip from YouTube using yt-dlp.
    Returns the path to the saved WAV file, or None if failed.
    """
    safe_name = "".join(c for c in f"{title}_{artist}" if c.isalnum() or c in " -_")[:50]
    out_path  = os.path.join(output_dir, f"{video_id}.wav")

    if os.path.exists(out_path):
        return out_path   # already downloaded

    url = f"https://www.youtube.com/watch?v={video_id}"

    ydl_opts = {
        "format":            "bestaudio/best",
        "outtmpl":           os.path.join(output_dir, f"{video_id}.%(ext)s"),
        "postprocessors":    [{
            "key":             "FFmpegExtractAudio",
            "preferredcodec":  "wav",
        }],
        "download_sections": [{"start_time": 0, "end_time": CLIP_SECS}],
        "ffmpeg_location":   FFMPEG_PATH,   # use imageio ffmpeg — no admin needed
        "quiet":             True,
        "no_warnings":       True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return out_path if os.path.exists(out_path) else None
    except Exception as e:
        return None


def extract_features_from_audio(wav_path, sr=SAMPLE_RATE):
    """
    Extracts audio features from a WAV file using librosa.

    Features extracted:
    - tempo          : BPM (beats per minute)
    - energy         : average loudness (RMS)
    - spectral_centroid : brightness
    - spectral_rolloff  : frequency below which 85% of energy lies
    - zero_crossing_rate: how often signal crosses zero (noisiness)
    - mfcc_1..13     : timbre features (like a fingerprint of the sound)
    - chroma_1..12   : which musical notes are present
    """
    try:
        audio, sr = librosa.load(wav_path, sr=sr, mono=True, duration=CLIP_SECS)

        # Tempo (BPM)
        tempo, _ = librosa.beat.beat_track(y=audio, sr=sr)

        # Energy (RMS = Root Mean Square amplitude)
        energy = float(np.mean(librosa.feature.rms(y=audio)))

        # Spectral features
        spec_centroid = float(np.mean(librosa.feature.spectral_centroid(y=audio, sr=sr)))
        spec_rolloff  = float(np.mean(librosa.feature.spectral_rolloff(y=audio, sr=sr)))
        zcr           = float(np.mean(librosa.feature.zero_crossing_rate(y=audio)))

        # MFCCs (13 coefficients — captures timbre/texture)
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        mfcc_means = {f"mfcc_{i+1}": float(np.mean(mfccs[i])) for i in range(13)}

        # Chroma (12 pitch classes — captures harmony/key)
        chroma = librosa.feature.chroma_stft(y=audio, sr=sr)
        chroma_means = {f"chroma_{i+1}": float(np.mean(chroma[i])) for i in range(12)}

        features = {
            "tempo":               float(tempo),
            "energy":              energy,
            "spectral_centroid":   spec_centroid,
            "spectral_rolloff":    spec_rolloff,
            "zero_crossing_rate":  zcr,
            **mfcc_means,
            **chroma_means,
        }
        return features, audio

    except Exception as e:
        return None, None


def build_feature_dataset(songs_df, max_songs=525):
    """
    Downloads audio and extracts features for all songs.
    max_songs limits how many songs to process (to save time).
    """
    print("=" * 65)
    print("  DOWNLOADING AUDIO & EXTRACTING FEATURES")
    print("=" * 65)
    print(f"  Processing up to {max_songs} songs...")
    print("  (This may take 10-15 minutes for 200 songs)\n")

    rows   = []
    audios = {}   # store audio arrays for mixing later

    for i, (_, row) in enumerate(songs_df.head(max_songs).iterrows()):
        video_id = row["video_id"]
        title    = row["title"]
        artist   = row["artist"]

        print(f"  [{i+1:03d}/{min(max_songs, len(songs_df))}] {title[:35]:<35} — {artist[:20]}", end=" ", flush=True)

        # Download
        wav_path = download_audio_clip(video_id, title, artist)
        if not wav_path:
            print("❌ download failed")
            continue

        # Extract features
        features, audio = extract_features_from_audio(wav_path)
        if features is None:
            print("❌ feature extraction failed")
            continue

        rows.append({
            "video_id":  video_id,
            "title":     title,
            "artist":    artist,
            "album":     row.get("album", ""),
            "wav_path":  wav_path,
            **features
        })
        audios[video_id] = audio
        print(f"✅  tempo={features['tempo']:.0f}bpm  energy={features['energy']:.4f}")

        time.sleep(0.1)

    features_df = pd.DataFrame(rows)
    features_df.to_csv("bollywood_features.csv", index=False)

    print(f"\n✅ Features extracted for {len(features_df)} songs")
    print(f"✅ Saved to bollywood_features.csv")
    return features_df, audios


# ── RUN ───────────────────────────────────────────────────────────────────────
features_df, audio_cache = build_feature_dataset(songs_df, max_songs=525)
print(features_df[["title", "artist", "tempo", "energy", "spectral_centroid"]].head(8).to_string(index=False))

# =============================================================================
#  BUILD THE BOLLYWOOD RECOMMENDER
#
#  Uses all extracted audio features:
#  tempo, energy, spectral features, MFCCs, chroma
#
#  Steps:
#  1. Normalise features (RobustScaler)
#  2. Reduce dimensions (PCA)
#  3. Build NearestNeighbors model (cosine similarity)
# =============================================================================

# All feature columns we use for similarity
FEATURE_COLS = (
    ["tempo", "energy", "spectral_centroid", "spectral_rolloff", "zero_crossing_rate"] +
    [f"mfcc_{i}" for i in range(1, 14)] +
    [f"chroma_{i}" for i in range(1, 13)]
)

# Keep only columns that exist
FEATURE_COLS = [c for c in FEATURE_COLS if c in features_df.columns]

def build_recommender(features_df, n_neighbors=15, use_pca=True):
    """
    Builds a content-based recommender from extracted audio features.

    1. RobustScaler   → normalise so no feature dominates
    2. PCA            → reduce noise, keep 95% of variance
    3. NearestNeighbors (cosine) → find similar songs
    """
    print("=" * 60)
    print("  BUILDING BOLLYWOOD RECOMMENDER")
    print("=" * 60)

    df_clean = features_df.dropna(subset=FEATURE_COLS).copy().reset_index(drop=True)
    print(f"  Songs with complete features: {len(df_clean)}")
    print(f"  Feature columns used: {len(FEATURE_COLS)}")

    X = df_clean[FEATURE_COLS].values

    # Normalise
    print("\n  Normalising features (RobustScaler)...")
    scaler   = RobustScaler()
    X_scaled = np.clip(scaler.fit_transform(X), -5, 5)

    # PCA
    pca = None
    if use_pca:
        n_comp = min(20, X_scaled.shape[1], X_scaled.shape[0] - 1)
        print(f"  Applying PCA ({n_comp} components)...")
        pca    = PCA(n_components=n_comp)
        X_final = pca.fit_transform(X_scaled)
        print(f"  ✓ Variance kept: {pca.explained_variance_ratio_.sum()*100:.1f}%")
    else:
        X_final = X_scaled

    # Build NearestNeighbors
    k = min(n_neighbors + 1, len(df_clean) - 1)
    print(f"\n  Building NearestNeighbors model (cosine, k={k})...")
    nn_model = NearestNeighbors(n_neighbors=k, metric="cosine", algorithm="auto")
    nn_model.fit(X_final)

    print(f"\n✅ Recommender ready!")
    print(f"   {len(df_clean)} songs indexed across {df_clean['artist'].nunique()} artists")

    return nn_model, X_final, df_clean, scaler, pca


nn_model, feat_matrix, songs_clean, scaler, pca = build_recommender(features_df)

# =============================================================================
#  RECOMMENDATION FUNCTION
# =============================================================================

def recommend_similar_songs(song_name, artist_name=None, n=10):
    """
    Finds Bollywood songs similar to the input song.

    song_name   : partial name match works (case-insensitive)
    artist_name : optionally filter by artist
    n           : number of recommendations to return
    """
    # Search for the song
    mask = songs_clean["title"].str.lower().str.contains(song_name.lower(), na=False)
    if artist_name:
        mask &= songs_clean["artist"].str.lower().str.contains(artist_name.lower(), na=False)

    matches = songs_clean[mask]
    if matches.empty:
        print(f"❌ Song '{song_name}' not found.")
        print("\n  Available songs (sample):")
        for t in songs_clean["title"].sample(min(10, len(songs_clean))):
            print(f"    - {t}")
        return None

    idx      = matches.index[0]
    song_row = matches.iloc[0]

    print(f"\n🎵 Input Song : {song_row['title']}")
    print(f"   Artist      : {song_row['artist']}")
    print(f"   Tempo       : {song_row['tempo']:.0f} BPM")
    print(f"   Energy      : {song_row['energy']:.4f}")
    print(f"   Brightness  : {song_row['spectral_centroid']:.0f} Hz")

    distances, indices = nn_model.kneighbors([feat_matrix[idx]])

    recs = []
    for dist, rec_idx in zip(distances[0][1:], indices[0][1:]):
        row = songs_clean.iloc[rec_idx]
        recs.append({
            "track_id":         row["video_id"],
            "title":            row["title"],
            "artist":           row["artist"],
            "similarity_score": round(float(1 - dist), 4),
            "tempo":            round(float(row["tempo"]), 1),
            "energy":           round(float(row["energy"]), 4),
            "wav_path":         row.get("wav_path", ""),
        })

    rec_df = pd.DataFrame(recs[:n])

    print(f"\n📋 Top {n} Similar Songs:")
    print("-" * 65)
    for i, r in rec_df.iterrows():
        has_audio = "🔊" if r["wav_path"] and os.path.exists(str(r["wav_path"])) else "  "
        print(f"  {i+1:2d}. {has_audio} {r['title'][:35]:<35} — {r['artist'][:20]:<20} ({r['similarity_score']:.3f})")

    print("\n  🔊 = audio file ready for mixing")
    return rec_df


# ── List available songs to choose from ───────────────────────────────────────
print("Available songs (sample — use any of these as INPUT_SONG):")
print(songs_clean[["title","artist"]].sample(min(15,len(songs_clean))).to_string(index=False))


INPUT_SONG = "zaalima"   # ← change this to any song in the dataset

rec_df = recommend_similar_songs(song_name=INPUT_SONG, n=20)
print(rec_df)

def evaluate_recommender(input_song_name, rec_df):
    """
    Evaluates the recommender based on:
    1. The input song itself
    2. The recommended songs for that input song
    3. How similar the recommendations are to each other (cohesion)
    """
    print("=" * 60)
    print("  RECOMMENDER EVALUATION")
    print(f"  Input Song: {input_song_name}")
    print("=" * 60)

    if rec_df is None or len(rec_df) == 0:
        print("❌ No recommendations to evaluate.")
        return

    # ── 1. Similarity of recommended songs to input song ─────────────
    print("\n  📊 Similarity to Input Song:")
    print(f"  {'-'*55}")
    sims = rec_df['similarity_score'].values
    for i, row in rec_df.iterrows():
        bar = "█" * int(row['similarity_score'] * 20)
        print(f"  {i+1:2d}. {row['title'][:30]:<30} {row['similarity_score']:.3f} {bar}")

    print(f"\n  Average Similarity  : {sims.mean():.4f}")
    print(f"  Highest Similarity  : {sims.max():.4f}  — {rec_df.loc[rec_df['similarity_score'].idxmax(), 'title']}")
    print(f"  Lowest Similarity   : {sims.min():.4f}  — {rec_df.loc[rec_df['similarity_score'].idxmin(), 'title']}")

    # ── 2. Artist diversity ───────────────────────────────────────────
    unique_artists = rec_df['artist'].nunique()
    total_songs    = len(rec_df)
    diversity      = unique_artists / total_songs
    print(f"\n  🎤 Artist Diversity:")
    print(f"  Unique Artists      : {unique_artists} out of {total_songs} songs")
    print(f"  Diversity Score     : {diversity:.2f}  (1.0 = all different artists)")
    for artist, count in rec_df['artist'].value_counts().items():
        print(f"    - {artist:<25} {count} song{'s' if count>1 else ''}")

    # ── 3. Audio feature cohesion among recommendations ───────────────
    print(f"\n  🎵 Audio Feature Cohesion (how similar recs are to each other):")
    indices = []
    for _, row in rec_df.iterrows():
        match = songs_clean[songs_clean['video_id'] == row['track_id']]
        if not match.empty:
            indices.append(match.index[0])

    if len(indices) >= 2:
        rec_features = feat_matrix[indices]
        from sklearn.metrics.pairwise import cosine_similarity
        sim_matrix   = cosine_similarity(rec_features)
        np.fill_diagonal(sim_matrix, 0)
        cohesion = sim_matrix.sum() / (len(indices) * (len(indices) - 1))
        print(f"  Cohesion Score      : {cohesion:.4f}  (higher = more cohesive mix)")

        # Tempo and energy spread
        tempos   = rec_df['tempo'].values
        energies = rec_df['energy'].values
        print(f"  Tempo Range         : {tempos.min():.0f} – {tempos.max():.0f} BPM  (avg {tempos.mean():.0f})")
        print(f"  Energy Range        : {energies.min():.3f} – {energies.max():.3f}  (avg {energies.mean():.3f})")
    else:
        cohesion = 0

    # ── 4. Overall verdict ────────────────────────────────────────────
    avg_sim = sims.mean()
    print(f"\n  {'='*55}")
    if avg_sim >= 0.7:
        verdict = "✅ EXCELLENT — Highly similar recommendations"
    elif avg_sim >= 0.5:
        verdict = "✓  GOOD — Reasonably similar recommendations"
    else:
        verdict = "⚠  MODERATE — Could be improved with more songs"
    print(f"  {verdict}")
    print(f"  {'='*55}")

    return {
        "avg_similarity": round(float(avg_sim), 4),
        "diversity":      round(float(diversity), 4),
        "cohesion":       round(float(cohesion), 4),
        "verdict":        verdict,
    }

# ── Run evaluation using INPUT_SONG recommendations ───────────────────────────
eval_metrics = evaluate_recommender(INPUT_SONG, rec_df)

# =============================================================================
#  SETTINGS
# =============================================================================

SAMPLE_RATE    = 44100
TARGET_LUFS    = -23.0
CROSSFADE_SECS = 8
OUTPUT_DIR     = "mix_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =============================================================================
#  AUDIO PROCESSING
# =============================================================================

def calculate_lufs(audio, sr):
    """Accurate LUFS with RMS fallback."""
    block_size = int(sr * 0.4)
    if len(audio) < block_size:
        rms = np.sqrt(np.mean(audio**2))
        return float(20 * np.log10(rms + 1e-10))
    try:
        b, a  = scipy_signal.butter(2, 1500/(sr/2), btype="high")
        w     = scipy_signal.lfilter(b, a, audio)
        b2,a2 = scipy_signal.butter(2, 38/(sr/2),   btype="high")
        w     = scipy_signal.lfilter(b2, a2, w)
        blocks = [w[i:i+block_size] for i in range(0, len(w)-block_size, block_size)]
        ms     = np.array([np.mean(b**2) for b in blocks])
        ms     = ms[ms > 1e-10]
        if len(ms) == 0:
            raise ValueError("K-weighting killed signal")
        lufs   = float(-0.691 + 10*np.log10(np.mean(ms)))
        rms_db = float(20 * np.log10(np.sqrt(np.mean(audio**2)) + 1e-10))
        if lufs < rms_db - 20:
            return rms_db
        return lufs
    except:
        rms = np.sqrt(np.mean(audio**2))
        return float(20 * np.log10(rms + 1e-10))


def normalise_volume(audio, sr, target=TARGET_LUFS):
    """
    Clean normalisation — NO compression, NO distortion.
    Simply scales audio so LUFS reaches target.
    Peak is always kept under 0.9 to prevent clipping.
    """
    audio = audio.copy().astype(np.float32)

    # Step 1 — remove DC offset
    audio = audio - np.mean(audio)

    # Step 2 — peak normalise to 0.9 (leave headroom)
    peak = np.max(np.abs(audio))
    if peak < 1e-6: return audio
    audio = audio / peak * 0.9

    # Step 3 — measure current LUFS and apply single clean gain
    current = calculate_lufs(audio, sr)
    if current <= -65 or current >= 0:
        return audio

    diff = target - current
    # Cap gain — never boost more than +12dB to avoid distortion
    diff = np.clip(diff, -20.0, 12.0)
    gain = 10 ** (diff / 20.0)
    audio = audio * gain

    # Step 4 — final peak safety — never exceed 0.9
    peak = np.max(np.abs(audio))
    if peak > 0.9:
        audio = audio * (0.9 / peak)

    return np.clip(audio, -0.99, 0.99).astype(np.float32)


def apply_eq(audio, sr, role):
    """
    Clarity-preserving EQ.
    All roles keep full frequency range — only gentle shaping.
    """
    nyq = sr / 2.0
    out = audio.copy()

    # All roles — remove only sub-bass rumble below 30Hz
    b,a = scipy_signal.butter(2, 30/nyq, btype="high")
    out = scipy_signal.lfilter(b, a, out)

    if role == "bass":
        # Gentle high rolloff — blend 30% low-passed with 70% original
        b,a = scipy_signal.butter(2, 8000/nyq, btype="low")
        out = scipy_signal.lfilter(b, a, out) * 0.3 + out * 0.7
    elif role == "treble":
        # Gentle low rolloff — blend 30% high-passed with 70% original
        b,a = scipy_signal.butter(2, 200/nyq, btype="high")
        out = scipy_signal.lfilter(b, a, out) * 0.3 + out * 0.7
    elif role == "mid":
        # Slight vocal presence boost — blend 20% band with 80% original
        b,a = scipy_signal.butter(2, [800/nyq, 4000/nyq], btype="band")
        out = scipy_signal.lfilter(b, a, out) * 0.2 + out * 0.8
    # full role — no additional EQ

    return out.astype(np.float32)


def mono_to_stereo(audio, pan):
    """Stereo panning with subtle Haas effect for width."""
    angle = (pan + 1.0) / 2.0 * (np.pi / 2)
    left  = np.cos(angle) * audio
    right = np.sin(angle) * audio
    delay_samples = int(0.010 * SAMPLE_RATE)   # 10ms — subtle
    if pan >= 0:
        right = np.concatenate([np.zeros(delay_samples), right[:-delay_samples]])
    else:
        left  = np.concatenate([np.zeros(delay_samples), left[:-delay_samples]])
    return np.stack([left, right]).astype(np.float32)


def detect_structure(audio, sr):
    """
    Detects structural sections: verse, chorus, bridge, intro, outro, instrumental.
    Uses RMS energy, ZCR and onset density.
    """
    hop     = int(sr * 1)
    window  = int(sr * 3)
    min_gap = int(sr * 5)   # lowered to 5s so more sections are detected

    timestamps = []
    for start in range(0, len(audio) - window, hop):
        chunk  = audio[start:start+window]
        rms    = float(np.sqrt(np.mean(chunk**2)))
        zcr    = float(np.mean(librosa.feature.zero_crossing_rate(y=chunk)))
        onsets = len(librosa.onset.onset_detect(y=chunk, sr=sr))
        timestamps.append({"start": start, "rms": rms, "zcr": zcr, "onsets": onsets})

    if not timestamps:
        return []

    rms_vals = np.array([t["rms"]    for t in timestamps])
    zcr_vals = np.array([t["zcr"]    for t in timestamps])
    on_vals  = np.array([t["onsets"] for t in timestamps])

    rms_med = np.median(rms_vals)
    zcr_med = np.median(zcr_vals)
    on_med  = np.median(on_vals)

    for t in timestamps:
        rms_high = t["rms"]    > rms_med * 1.2
        rms_low  = t["rms"]    < rms_med * 0.7
        zcr_high = t["zcr"]    > zcr_med * 1.1
        zcr_low  = t["zcr"]    < zcr_med * 0.85
        on_high  = t["onsets"] > on_med  * 1.2

        if zcr_low and rms_high:
            t["type"] = "instrumental_chorus"
        elif zcr_low and not rms_low:
            t["type"] = "instrumental"
        elif rms_high and zcr_high and on_high:
            t["type"] = "chorus"
        elif rms_low and zcr_low:
            t["type"] = "intro_outro"
        elif zcr_high:
            t["type"] = "verse"
        else:
            t["type"] = "bridge"

    sections  = []
    cur_type  = timestamps[0]["type"]
    cur_start = timestamps[0]["start"]
    cur_rmss  = [timestamps[0]["rms"]]
    cur_zcrs  = [timestamps[0]["zcr"]]

    for t in timestamps[1:]:
        if t["type"] == cur_type:
            cur_rmss.append(t["rms"])
            cur_zcrs.append(t["zcr"])
        else:
            end = t["start"]
            if end - cur_start >= min_gap * sr:
                chunk = audio[cur_start:end]
                try:
                    tempo, _ = librosa.beat.beat_track(y=chunk, sr=sr)
                    bpm = float(tempo)
                except:
                    bpm = 0.0
                sections.append({
                    "start":         cur_start,
                    "end":           end,
                    "type":          cur_type,
                    "bpm":           bpm,
                    "avg_rms":       float(np.mean(cur_rmss)),
                    "avg_zcr":       float(np.mean(cur_zcrs)),
                    "vocal_density": float(np.mean(cur_zcrs)),
                })
            cur_type  = t["type"]
            cur_start = t["start"]
            cur_rmss  = [t["rms"]]
            cur_zcrs  = [t["zcr"]]

    end = len(audio)
    if end - cur_start >= min_gap * sr:
        chunk = audio[cur_start:end]
        try:
            tempo, _ = librosa.beat.beat_track(y=chunk, sr=sr)
            bpm = float(tempo)
        except:
            bpm = 0.0
        sections.append({
            "start":         cur_start,
            "end":           end,
            "type":          cur_type,
            "bpm":           bpm,
            "avg_rms":       float(np.mean(cur_rmss)),
            "avg_zcr":       float(np.mean(cur_zcrs)),
            "vocal_density": float(np.mean(cur_zcrs)),
        })

    return sections


def find_best_entry_point(audio, sr, target_bpm, min_secs=60, max_secs=200):
    """
    Finds best section to include in mashup.
    Priority: instrumental_chorus > instrumental > chorus > verse > bridge > intro_outro
    BPM proximity is tiebreaker within each tier.
    """
    sections = detect_structure(audio, sr)

    if not sections:
        seg_len = min(int(sr * min_secs), len(audio))
        return 0, seg_len, audio[:seg_len].astype(np.float32)

    priority = {
        "instrumental_chorus": 0,
        "instrumental":        1,
        "chorus":              2,
        "bridge":              3,
        "verse":               4,
        "intro_outro":         5,
    }

    min_len = int(sr * min_secs)
    max_len = int(sr * max_secs)

    best       = None
    best_score = 9999

    for sec in sections:
        sec_len = sec["end"] - sec["start"]
        if sec_len < min_len:
            continue
        tier = priority.get(sec["type"], 5)
        if target_bpm > 0 and sec["bpm"] > 0:
            bpm_diff = min(
                abs(sec["bpm"] - target_bpm),
                abs(sec["bpm"] - target_bpm * 2),
                abs(sec["bpm"] - target_bpm / 2),
            )
        else:
            bpm_diff = 50
        score = tier * 100 + bpm_diff
        if score < best_score:
            best_score = score
            best       = sec

    if best is None:
        for sec in sections:
            tier     = priority.get(sec["type"], 5)
            bpm_diff = abs(sec["bpm"] - target_bpm) if target_bpm > 0 else 50
            score    = tier * 100 + bpm_diff
            if best is None or score < best_score:
                best_score = score
                best       = sec

    start = best["start"]
    end   = min(best["end"], start + max_len)
    end   = max(end, start + int(sr * 10))

    segment = audio[start:end].astype(np.float32)
    return start, end, segment


print("✅ Audio processing functions defined")
print("   ✓ Clean normalisation — no compression, no distortion")
print("   ✓ Peak always capped at 0.9 — no clipping")
print("   ✓ Clarity-preserving EQ — gentle blending only")
print("   ✓ Song structure detection")
print("   ✓ BPM-aware entry point selection")

TRACK_ROLES = ["full", "mid", "bass", "treble", "mid", "full"]
TRACK_PANS  = [0.0, -0.6, 0.5, -0.5, 0.6, -0.3]


def load_tracks_for_mixing(input_song_row, rec_df, audio_cache, max_tracks=6):
    """
    Loads audio for mixing.
    INPUT SONG is always Track 1.
    Remaining tracks are top recommendations with audio available.
    Normalises every track before adding to mix pipeline.
    """
    print("\n" + "="*60)
    print("  LOADING AUDIO FOR MIXING")
    print("="*60)

    loaded = []

    # ── Track 1: Input song (always first) ────────────────────────────
    print(f"\n  Track 1 (INPUT): {input_song_row['title']} — {input_song_row['artist']}")
    input_vid   = input_song_row["video_id"]
    input_audio = audio_cache.get(input_vid)
    if input_audio is None:
        wav = input_song_row.get("wav_path", "")
        if wav and os.path.exists(str(wav)):
            try: input_audio, _ = librosa.load(wav, sr=SAMPLE_RATE, mono=True)
            except: input_audio = None
    if input_audio is not None:
        # Normalise before mixing
        input_audio = normalise_volume(input_audio, SAMPLE_RATE, TARGET_LUFS)
        input_tempo, _ = librosa.beat.beat_track(
            y=input_audio[:SAMPLE_RATE*30], sr=SAMPLE_RATE
        )
        input_tempo = float(input_tempo)
        loaded.append({
            "track_id":  input_vid,
            "title":     input_song_row["title"],
            "artist":    input_song_row["artist"],
            "similarity":1.0,
            "tempo":     input_tempo,
            "energy":    float(np.sqrt(np.mean(input_audio**2))),
            "audio":     input_audio.astype(np.float32),
            "sr":        SAMPLE_RATE,
            "is_input":  True,
        })
        print(f"    ✓ Loaded  tempo={input_tempo:.0f} BPM  "
              f"duration={len(input_audio)/SAMPLE_RATE:.0f}s  "
              f"lufs={calculate_lufs(input_audio, SAMPLE_RATE):.1f}")
    else:
        print(f"    ✗ Input song audio not found")
        input_tempo = 120.0

    # ── Tracks 2-6: Recommendations ───────────────────────────────────
    candidates = rec_df[
        rec_df["wav_path"].notna() & (rec_df["wav_path"] != "")
    ].copy()

    for _, row in candidates.iterrows():
        if len(loaded) >= max_tracks: break
        vid   = row["track_id"]
        title = row["title"]
        print(f"\n  Track {len(loaded)+1}: {title[:40]} — {row['artist']}")
        audio = audio_cache.get(vid)
        if audio is None:
            wp = row.get("wav_path", "")
            if wp and os.path.exists(str(wp)):
                try: audio, _ = librosa.load(wp, sr=SAMPLE_RATE, mono=True)
                except: audio = None
        if audio is None:
            print(f"    ✗ No audio, skipping")
            continue

        # Normalise before mixing
        audio = normalise_volume(audio, SAMPLE_RATE, TARGET_LUFS)

        try:
            tempo, _ = librosa.beat.beat_track(
                y=audio[:SAMPLE_RATE*30], sr=SAMPLE_RATE
            )
            tempo = float(tempo)
        except:
            tempo = float(row.get("tempo", 120))

        loaded.append({
            "track_id":  vid,
            "title":     title,
            "artist":    row["artist"],
            "similarity":float(row["similarity_score"]),
            "tempo":     tempo,
            "energy":    float(np.sqrt(np.mean(audio**2))),
            "audio":     audio.astype(np.float32),
            "sr":        SAMPLE_RATE,
            "is_input":  False,
        })
        print(f"    ✓ Loaded  tempo={tempo:.0f} BPM  "
              f"duration={len(audio)/SAMPLE_RATE:.0f}s  "
              f"lufs={calculate_lufs(audio, SAMPLE_RATE):.1f}  "
              f"similarity={row['similarity_score']:.3f}")

    print(f"\n  {'✅' if loaded else '❌'}  {len(loaded)} tracks ready")
    return loaded


def mix_all_tracks(tracks, sr, crossfade_secs=CROSSFADE_SECS, target_lufs=TARGET_LUFS):
    """
    Natural DJ-style mashup:
    - NO fixed segment length — each song plays as long as it naturally should
    - NO speed change — original pace of every song fully preserved
    - Cuts happen at natural tune/instrumental section boundaries
    - Entry point chosen where local BPM matches input song BPM
    - Variable lengths: one song might play 30s, another 90s
    """
    print("\n" + "="*60)
    print("  MIXING — NATURAL DJ STYLE (NO SPEED CHANGE)")
    print("="*60)

    input_tempo = tracks[0]["tempo"] if tracks else 120.0
    print(f"\n  Reference BPM : {input_tempo:.0f} (input song)")
    print(f"  Crossfade     : {crossfade_secs}s")
    print(f"  Segment length: VARIABLE — natural section boundaries")
    print(f"  Speed change  : DISABLED")

    cf  = int(sr * crossfade_secs)
    fi  = np.linspace(0, 1, cf, dtype=np.float32)
    fo  = np.linspace(1, 0, cf, dtype=np.float32)
    processed = []

    for i, track in enumerate(tracks):
        role     = TRACK_ROLES[i % len(TRACK_ROLES)]
        pan      = TRACK_PANS[i % len(TRACK_PANS)]
        is_input = track.get("is_input", False)
        audio    = track["audio"].copy()

        print(f"\n  Track {i+1}: {track['title'][:40]}")
        print(f"    Artist : {track['artist']}")
        print(f"    BPM    : {track['tempo']:.0f}  |  Role: {role}  |  Pan: {pan:+.2f}")

        # ── Find best entry point — variable length, no speed change ──
        start, end, segment = find_best_entry_point(
            audio, sr,
            target_bpm=input_tempo,
            min_secs=60,
            max_secs=200
        )

        seg_duration = len(segment) / sr
        sections     = detect_structure(audio, sr)
        picked_type  = "unknown"
        for sec in sections:
            if sec["start"] == start:
                picked_type = sec["type"]
                break
        print(f"    Entry  : {start/sr:.1f}s to {end/sr:.1f}s ({seg_duration:.1f}s) | section={picked_type} {'[INPUT]' if is_input else ''}")

        # ── Normalise loudness ─────────────────────────────────────────
        segment = normalise_volume(segment, sr, target_lufs)
        lufs    = calculate_lufs(segment, sr)
        print(f"    Loudness: {lufs:.1f} LUFS")

        # ── EQ ─────────────────────────────────────────────────────────
        segment = apply_eq(segment, sr, role)

        # ── Stereo pan ─────────────────────────────────────────────────
        stereo = mono_to_stereo(segment, pan)
        processed.append(stereo)

    # ── Join with crossfades ───────────────────────────────────────────
    print("\n  Joining tracks with crossfades...")
    mix = processed[0].copy()
    if mix.shape[1] >= cf:
        mix[:, -cf:] *= fo

    for stereo in processed[1:]:
        inc = stereo.copy()
        if inc.shape[1] >= cf:
            inc[:, :cf] *= fi
        os_ = max(0, mix.shape[1] - cf)
        bl  = min(mix.shape[1] - os_, cf, inc.shape[1])
        # Reduce blend gain to preserve dynamic range
        blended = (mix[:, os_:os_+bl] * 0.6) + (inc[:, :bl] * 0.6)
        mix = np.concatenate([mix[:, :os_], blended, inc[:, bl:]], axis=1)
        if mix.shape[1] >= cf:
            mix[:, -cf:] *= fo

    # ── Final LUFS correction + limiter ───────────────────────────────
   # ── Final LUFS correction + limiter ───────────────────────────────
   # ── Final clean master ─────────────────────────────────────────────
    mono_mix   = np.mean(mix, axis=0)
    final_lufs = calculate_lufs(mono_mix, sr)
    print(f"\n  Pre-master LUFS : {final_lufs:.1f}")

    # Single clean gain — no iterative loop that causes distortion
    if final_lufs > -65:
        diff = TARGET_LUFS - final_lufs
        diff = np.clip(diff, -20.0, 10.0)   # max +10dB boost
        gain = 10 ** (diff / 20.0)
        mix  = mix * gain
        print(f"  ✓ Master gain : {gain:.3f}x  ({diff:+.1f} dB)")

    # Peak safety — never exceed 0.9
    peak = np.max(np.abs(mix))
    if peak > 0.9:
        mix = mix * (0.9 / peak)
        print(f"  ✓ Peak limited to 0.9")

    final_lufs_check = calculate_lufs(np.mean(mix, axis=0), sr)
    rms_check        = 20 * np.log10(np.sqrt(np.mean(mix**2)) + 1e-10)
    print(f"  Post-master LUFS : {final_lufs_check:.1f}")
    print(f"  Post-master RMS  : {rms_check:.1f} dB")

    duration = mix.shape[1] / sr
    print(f"\n  ✅ Mix complete!  Duration: {duration:.1f}s  ({duration/60:.1f} min)")
    return mix.astype(np.float32)

print("✅ Mixing engine defined")
print("   ✓ Pre-normalisation of every track before mixing")
print("   ✓ Variable segment length — natural section boundaries")
print("   ✓ No speed change — original pace preserved")
print("   ✓ No lyric cuts — prefers instrumental/chorus sections")
print("   ✓ BPM-aware entry point for each song")
print("   ✓ Reduced crossfade gain to preserve dynamic range")
print("   ✓ Final LUFS correction on full mix")

def measure_dynamic_range(mix, sr):
    """Loud vs quiet difference. Higher = more natural. (MixAssist 2025)"""
    mono = mix.mean(axis=0); bs = int(sr*0.5)
    rms  = [np.sqrt(np.mean(mono[i:i+bs]**2)) for i in range(0,len(mono)-bs,bs)]
    if len(rms) < 5: return 0.0
    rms = sorted(rms); n = max(1,len(rms)//5)
    return float(20*np.log10(np.mean(rms[-n:])/(np.mean(rms[:n])+1e-9)))

def measure_spectral_centroid(mix, sr):
    """Average frequency Hz. Higher = brighter. (Agwan et al. 2023)"""
    mono = mix.mean(axis=0); bs = int(sr*0.5); cs = []
    for i in range(0,len(mono)-bs,bs):
        chunk = mono[i:i+bs]*np.hanning(bs)
        mags  = np.abs(np.fft.rfft(chunk))
        freqs = np.fft.rfftfreq(bs, d=1.0/sr)
        if mags.sum()>1e-9: cs.append(np.dot(freqs,mags)/mags.sum())
    return float(np.mean(cs)) if cs else 0.0

def measure_stereo_width(mix):
    """L vs R difference. 0=mono, 1=wide. (Katyal et al. 2024)"""
    l,r = mix[0], mix[1]
    if np.std(l)<1e-9 or np.std(r)<1e-9: return 0.0
    return float(1.0 - abs(np.corrcoef(l,r)[0,1]))

def measure_clipping_rate(mix, threshold=0.99):
    """% distorted samples. Should be 0%. (Vanka et al. 2023)"""
    return float((np.sum(np.abs(mix)>threshold)/mix.size)*100)

def evaluate_mix(final_mix, tracks, sr):
    """Runs all 5 metrics and computes quality score (0-100)."""
    print("\n" + "="*60)
    print("  EVALUATING THE MIX")
    print("="*60)

    mono       = final_mix.mean(axis=0)
    lufs_mono  = calculate_lufs(mono, sr)
    lufs_left  = calculate_lufs(final_mix[0], sr)
    lufs_right = calculate_lufs(final_mix[1], sr)
    best_lufs  = max(lufs_mono, lufs_left, lufs_right)

    m = {
        "integrated_lufs":      calculate_lufs(mono, sr),
        "dynamic_range_db":     measure_dynamic_range(final_mix, sr),
        "spectral_centroid_hz": measure_spectral_centroid(final_mix, sr),
        "stereo_width":         measure_stereo_width(final_mix),
        "clipping_rate_pct":    measure_clipping_rate(final_mix),
        "duration_seconds":     final_mix.shape[1]/sr,
    }

    print(f"\n  {'Metric':<28} {'Value':<24} Paper")
    print(f"  {'-'*68}")
    print(f"  {'1. Integrated LUFS':<28} {m['integrated_lufs']:.1f} dBFS (target {TARGET_LUFS})   Vanka et al. 2023")
    print(f"  {'2. Dynamic Range':<28} {m['dynamic_range_db']:.1f} dB                      MixAssist 2025")
    print(f"  {'3. Spectral Centroid':<28} {m['spectral_centroid_hz']:.0f} Hz                     Agwan et al. 2023")
    print(f"  {'4. Stereo Width':<28} {m['stereo_width']:.3f} (0=mono, 1=wide)      Katyal et al. 2024")
    print(f"  {'5. Clipping Rate':<28} {m['clipping_rate_pct']:.4f} %                    Vanka et al. 2023")
    print(f"  {'Duration':<28} {m['duration_seconds']:.1f} s")

    per_track = []
    print(f"\n  Per-Track Loudness (target={TARGET_LUFS}):")
    for t in tracks:
        tl = calculate_lufs(t["audio"], sr)
        flag = "✅" if abs(tl-TARGET_LUFS)<3 else "⚠ "
        print(f"    {flag}  {t['title'][:38]:<38}  {tl:.1f} LUFS")
        per_track.append({"track_id":t["track_id"],"title":t["title"],
                           "artist":t["artist"],"lufs":round(tl,2),"similarity":t["similarity"]})
    m["per_track"] = per_track

    # ── NEW SCORE FORMULA ──────────────────────────────────────────────
    lufs_diff   = abs(m["integrated_lufs"] - TARGET_LUFS)
    lufs_score  = max(0, 35 - lufs_diff * 2)
    dr          = m["dynamic_range_db"]
    dr_score    = max(0, min(25, dr * 1.5)) if dr >= 3 else 0
    width_score = m["stereo_width"] * 20
    clip_score  = max(0, 10 - m["clipping_rate_pct"] * 50)
    sc          = m["spectral_centroid_hz"]
    if 1000 <= sc <= 3500:
        spec_score = 10.0
    elif sc < 1000:
        spec_score = max(0, 10 - (1000 - sc) / 100)
    else:
        spec_score = max(0, 10 - (sc - 3500) / 200)

    score = round(max(0, min(100,
        lufs_score + dr_score + width_score + clip_score + spec_score)), 1)

    m["quality_score"] = score
    m["score_breakdown"] = {
        "lufs_score":  round(lufs_score, 1),
        "dr_score":    round(dr_score, 1),
        "width_score": round(width_score, 1),
        "clip_score":  round(clip_score, 1),
        "spec_score":  round(spec_score, 1),
    }
    m["verdict"] = (
        "✅ EXCELLENT" if score >= 80 else
        "✓  GOOD"     if score >= 65 else
        "⚠  MODERATE" if score >= 50 else
        "✗  POOR"
    )

    print(f"\n  Score Breakdown:")
    print(f"    LUFS Score    : {lufs_score:.1f} / 35")
    print(f"    Dynamic Range : {dr_score:.1f} / 25")
    print(f"    Stereo Width  : {width_score:.1f} / 20")
    print(f"    No Clipping   : {clip_score:.1f} / 10")
    print(f"    Spectral      : {spec_score:.1f} / 10")
    print(f"\n  🏆  Quality Score: {score} / 100  —  {m['verdict']}")
    return m

print("✅ Evaluation functions defined")

def save_wav(final_mix, sr, output_dir=OUTPUT_DIR):
    path = os.path.join(output_dir, "bollywood_mix.wav")
    try:
        wavfile.write(path, sr, (final_mix.T*32767).astype(np.int16))
        print(f"  ✅ Audio saved → {path}")
        return path
    except Exception as e:
        print(f"  ⚠ Could not save WAV: {e}"); return ""

def save_report(metrics, tracks, output_dir=OUTPUT_DIR):
    report = {
        "mix_metrics":   {k:v for k,v in metrics.items() if k!="per_track"},
        "per_track":     metrics.get("per_track",[]),
        "tracks_in_mix": [{"track_id":t["track_id"],"title":t["title"],
                           "artist":t["artist"],"similarity":t["similarity"]} for t in tracks],
        "metric_explanations": {
            "integrated_lufs":      "Overall loudness. Target -14 dBFS. Ref: Vanka et al. 2023",
            "dynamic_range_db":     "Loud vs quiet. Higher=natural. Ref: MixAssist 2025",
            "spectral_centroid_hz": "Avg frequency. Higher=brighter. Ref: Agwan et al. 2023",
            "stereo_width":         "L vs R diff. 0=mono,1=wide. Ref: Katyal et al. 2024",
            "clipping_rate_pct":    "% distorted. Should be 0. Ref: Vanka et al. 2023",
            "quality_score":        "Composite score 0-100.",
        }
    }
    path = os.path.join(output_dir, "mix_report.json")
    with open(path,"w") as f: json.dump(report,f,indent=2)
    print(f"  ✅ Report saved → {path}")
    return path

def plot_mix_analysis(final_mix, tracks, metrics, sr, output_dir=OUTPUT_DIR):
    print("\n  Generating analysis chart...")
    fig, axes = plt.subplots(2,2,figsize=(16,10),facecolor="#1a1a2e")
    fig.suptitle("🎵  Bollywood AI Mix — Analysis Dashboard",
                 color="white",fontsize=16,fontweight="bold",y=0.99)
    ax1,ax2,ax3,ax4 = axes[0][0],axes[0][1],axes[1][0],axes[1][1]
    for ax in [ax1,ax2,ax3,ax4]:
        ax.set_facecolor("#16213e")
        for s in ax.spines.values(): s.set_color("#444")
        ax.tick_params(colors="#aaa")

    # Waveform
    t = np.linspace(0,final_mix.shape[1]/sr,final_mix.shape[1])
    step = max(1,len(t)//5000)
    ax1.plot(t[::step],final_mix[0][::step],color="#00b4d8",alpha=0.7,lw=0.5,label="Left")
    ax1.plot(t[::step],final_mix[1][::step],color="#e040fb",alpha=0.6,lw=0.5,label="Right")
    ax1.axhline(0.99,color="#ff6b6b",lw=0.8,ls="--",alpha=0.7,label="Clip limit")
    ax1.axhline(-0.99,color="#ff6b6b",lw=0.8,ls="--",alpha=0.7)
    ax1.set_title("Waveform",color="white",pad=8)
    ax1.set_xlabel("Time (s)",color="#aaa"); ax1.set_ylabel("Amplitude",color="#aaa")
    ax1.legend(fontsize=7,facecolor="#16213e",labelcolor="white")

    # Spectrogram
    mono = final_mix.mean(axis=0); n_fft,hop = 1024,256
    frames = [mono[i:i+n_fft]*np.hanning(n_fft) for i in range(0,len(mono)-n_fft,hop)]
    mag_db = 20*np.log10(np.abs(np.array([np.fft.rfft(f) for f in frames])).T+1e-9)
    ax2.imshow(mag_db,aspect="auto",origin="lower",cmap="magma",
               extent=[0,final_mix.shape[1]/sr,0,sr/2],vmin=-80,vmax=0)
    ax2.set_yscale("log"); ax2.set_ylim(50,sr/2)
    ax2.set_title("Spectrogram",color="white",pad=8)
    ax2.set_xlabel("Time (s)",color="#aaa"); ax2.set_ylabel("Frequency (Hz)",color="#aaa")

    # Per-track LUFS
    pt = metrics.get("per_track",[])
    labels = [f"{p['title'][:18]}—{p['artist'][:10]}" for p in pt]
    lvals  = [p["lufs"] for p in pt]
    colors = ["#06d6a0" if abs(v-TARGET_LUFS)<3 else "#ef476f" for v in lvals]
    ax3.barh(range(len(labels)),lvals,color=colors,edgecolor="#333",height=0.6)
    ax3.axvline(TARGET_LUFS,color="white",lw=1.5,ls="--",label=f"Target ({TARGET_LUFS})")
    ax3.set_yticks(range(len(labels))); ax3.set_yticklabels(labels,color="#ccc",fontsize=7)
    ax3.set_xlabel("Loudness (LUFS)",color="#aaa")
    ax3.set_title("Per-Track Loudness vs Target",color="white",pad=8)
    ax3.legend(fontsize=8,facecolor="#16213e",labelcolor="white")

    # Metrics table
    ax4.axis("off")
    rows = [
        ["METRIC","VALUE","PAPER"],
        ["Integrated LUFS",  f"{metrics['integrated_lufs']:.1f} dBFS","Vanka et al. 2023"],
        ["Dynamic Range",    f"{metrics['dynamic_range_db']:.1f} dB", "MixAssist 2025"],
        ["Spectral Centroid",f"{metrics['spectral_centroid_hz']:.0f} Hz","Agwan et al. 2023"],
        ["Stereo Width",     f"{metrics['stereo_width']:.3f}",         "Katyal et al. 2024"],
        ["Clipping Rate",    f"{metrics['clipping_rate_pct']:.4f} %",  "Vanka et al. 2023"],
        ["Quality Score",    f"{metrics['quality_score']} / 100",      "Composite"],
    ]
    col_x,row_h = [0.02,0.44,0.72],0.115
    for ri,rv in enumerate(rows):
        y  = 0.95-ri*row_h
        bg = "#0f3460" if ri==0 else ("#1e3a5f" if ri%2 else "#16213e")
        ax4.add_patch(plt.Rectangle((0,y-row_h*0.9),1,row_h*0.85,
                                    transform=ax4.transAxes,color=bg,zorder=0))
        for text,x in zip(rv,col_x):
            ax4.text(x,y-row_h*0.1,text,transform=ax4.transAxes,
                     color="#ffd166" if ri==0 else "white",
                     fontsize=8.5,fontweight="bold" if ri==0 else "normal",va="top")
    ax4.set_title("Evaluation Metrics (Research-Grounded)",color="white",pad=8)
    ax4.text(0.02,0.04,metrics.get("verdict",""),
             transform=ax4.transAxes,color="#06d6a0",fontsize=9,fontweight="bold")

    plt.tight_layout(rect=[0,0,1,0.97])
    path = os.path.join(output_dir,"mix_analysis.png")
    plt.savefig(path,dpi=140,bbox_inches="tight",facecolor=fig.get_facecolor())
    plt.close()
    print(f"  ✅ Chart saved → {path}")
    return path

print("✅ Save functions defined")

# =============================================================================
#  SONG SELECTION — Change INPUT_SONG and run this cell first
# =============================================================================

AUTO_SELECT = False        # ← True = auto pick top 5, False = you pick by number

# ── Get recommendations ───────────────────────────────────────────────────────
rec_df = recommend_similar_songs(song_name=INPUT_SONG, n=20)

if rec_df is None or len(rec_df) == 0:
    print("❌ Song not found.")
else:
    print(f"\n  Recommendations for: {INPUT_SONG}")
    print(f"  {'No.':<5} {'Title':<45} {'Artist':<25} {'Similarity'}")
    print(f"  {'-'*4} {'-'*44} {'-'*24} {'-'*10}")
    for i, (_, row) in enumerate(rec_df.iterrows()):
        print(f"  {i+1:<5} {row['title'][:44]:<45} {row['artist'][:24]:<25} {row['similarity_score']:.3f}")

    if AUTO_SELECT:
        SELECTED_INDICES = list(range(1, 6))   # auto = top 5
        print(f"\n✅ AUTO mode — top 5 songs selected")
    else:
        print(f"\n  Enter the numbers of songs you want in the mashup (e.g. 1 3 5 7 9)")
        print(f"  Pick up to 5 songs — press Enter when done")
        user_input      = input("  Your selection: ").strip()
        SELECTED_INDICES = [int(x) for x in user_input.split() if x.isdigit()]
        SELECTED_INDICES = [i for i in SELECTED_INDICES if 1 <= i <= len(rec_df)][:5]

    MANUAL_SONGS = rec_df.iloc[[i-1 for i in SELECTED_INDICES]]["title"].tolist()

    print(f"\n  Songs selected for mashup:")
    for i, title in enumerate(MANUAL_SONGS):
        row = rec_df[rec_df["title"] == title]
        sim = row["similarity_score"].values[0] if not row.empty else 0
        print(f"  {i+1}. {title:<45} similarity={sim:.3f}")
    print(f"\n✅ Done — now run Cell 29 to mix")

# =============================================================================
#  ▶  COMPLETE PIPELINE — Change INPUT_SONG and run this cell
# =============================================================================

# ── Step 1: Recommend ────────────────────────────────────────────────────────
rec_df = recommend_similar_songs(song_name=INPUT_SONG, n=20)

if rec_df is None or len(rec_df) == 0:
    print("❌ Song not found. Check available songs above.")
else:
    # ── Step 2: Find input song row in dataset ───────────────────────
    input_match = songs_clean[
        songs_clean["title"].str.lower().str.contains(INPUT_SONG.lower(), na=False)
    ]
    if input_match.empty:
        print("❌ Input song not in features dataset.")
    else:
        input_song_row = input_match.iloc[0].to_dict()
        if "wav_path" not in input_song_row:
            input_song_row["wav_path"] = os.path.join(
                AUDIO_DIR, f"{input_song_row['video_id']}.wav"
            )
        print(f"\n✅ Input song confirmed: {input_song_row['title']} — {input_song_row['artist']}")

        # ── Step 3: Evaluate recommender ────────────────────────────
        eval_metrics = evaluate_recommender(INPUT_SONG, rec_df)

        # ── Step 4: Filter rec_df based on user selection ────────────
        if AUTO_SELECT:
            filtered_rec_df = rec_df.head(5)
            print(f"\n✅ AUTO mode — top 5 songs selected by similarity")
        else:
            filtered_rec_df = rec_df[
                rec_df["title"].str.lower().isin([s.lower() for s in MANUAL_SONGS])
            ]
            print(f"\n✅ MANUAL mode — {len(filtered_rec_df)} songs matched from your selection")
            for s in MANUAL_SONGS:
                if s.lower() not in rec_df["title"].str.lower().values:
                    print(f"  ⚠  '{s}' not found in recommendations — skipping")

        print(f"\n  Songs going into mashup:")
        for i, (_, row) in enumerate(filtered_rec_df.iterrows()):
            print(f"  {i+1}. {row['title']:<40} similarity={row['similarity_score']:.3f}")

        # ── Step 5: Load audio (input song first + selected recommendations) ─
        tracks_for_mixing = load_tracks_for_mixing(
            input_song_row, filtered_rec_df, audio_cache, max_tracks=5
        )

        if not tracks_for_mixing:
            print("❌ No audio available for mixing.")
        else:
            # ── Step 6: BPM-matched mix ──────────────────────────────
            final_mix = mix_all_tracks(tracks_for_mixing, sr=SAMPLE_RATE)

            # ── Step 7: Evaluate mix ─────────────────────────────────
            mix_metrics = evaluate_mix(final_mix, tracks_for_mixing, sr=SAMPLE_RATE)

            # ── Step 8: Save outputs ─────────────────────────────────
            print("\n" + "="*50)
            print("  SAVING OUTPUTS")
            print("="*50)
            audio_path  = save_wav(final_mix, SAMPLE_RATE)
            plot_path   = plot_mix_analysis(final_mix, tracks_for_mixing, mix_metrics, SAMPLE_RATE)
            report_path = save_report(mix_metrics, tracks_for_mixing)

            # ── Step 9: Final summary ────────────────────────────────
            print(f"\n{'='*50}")
            print(f"  FINAL RESULTS FOR: {INPUT_SONG.upper()}")
            print(f"{'='*50}")
            print(f"  Mode               : {'AUTO' if AUTO_SELECT else 'MANUAL'}")
            print(f"  Tracks in mashup   : {len(tracks_for_mixing)}")
            print(f"  Track 1 (input)    : {tracks_for_mixing[0]['title']} — {tracks_for_mixing[0]['artist']}")
            print(f"  Mashup duration    : {final_mix.shape[1]/SAMPLE_RATE:.1f}s  ({final_mix.shape[1]/SAMPLE_RATE/60:.1f} min)")
            print(f"  Reference BPM      : {tracks_for_mixing[0]['tempo']:.0f}")
            print(f"  Quality Score      : {mix_metrics['quality_score']} / 100  —  {mix_metrics['verdict']}")
            print(f"  Integrated LUFS    : {mix_metrics['integrated_lufs']:.1f} dBFS")
            print(f"  Dynamic Range      : {mix_metrics['dynamic_range_db']:.1f} dB")
            print(f"  Stereo Width       : {mix_metrics['stereo_width']:.3f}")
            print(f"  Clipping Rate      : {mix_metrics['clipping_rate_pct']:.4f} %")
            print(f"  Rec Avg Similarity : {eval_metrics['avg_similarity']:.4f}")
            print(f"  Artist Diversity   : {eval_metrics['diversity']:.2f}")

            # ── Step 10: Play ─────────────────────────────────────────
            import IPython.display as ipd
            print(f"\n▶ Playing mashup...")
            display(ipd.Audio(final_mix, rate=SAMPLE_RATE))
